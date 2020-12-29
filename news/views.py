from django.shortcuts import render
import requests
import pickle
import os
from bs4 import BeautifulSoup
from news.models import News , Category
from django.db import IntegrityError
from news.algo import Algo,Multi

# object creation of Multi nomial algorithm class
pre = Multi()
pre.multi_N()
# Create your views here.
######   Scraping the timesofindia  news heading
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []
i=0

for th in toi_headings:
    if i > 1:
        
        toi_news.append(th.text)
    i+=1
    

#image scraping from TOI news
m_links = []
mg_class = toi_soup.find_all(class_="posrel")
for im in mg_class:
    img_tag = im.find("img")
    src = img_tag['data-src']
    m_links.append(src)
    
#news soure link 
f_links = []
for im in toi_headings:
    a_tag = im.find('a')
#     link = a_tag['href']
    if im.find('a'):
        link = a_tag.attrs['href']
        st = 'https://timesofindia.indiatimes.com'+link
        f_links.append(st)
# Below code combine the headings and image of  timesofindia in combine_l list  
combine_l = []
for h, l ,s in zip(toi_news, m_links,f_links):
    combine_l.append((h,l,s))
    

#Getting news from Indian Express times

ht_r = requests.get("https://indianexpress.com/section/india/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.find_all('h2')

ht_news = []

# Below code is for scraping heading text clearly and appending them within list.
for hth in ht_headings: 
    a_tag = hth.find('a')
    ht_news.append(a_tag.text)
    
# For image scrapping of inadian indianexpress   
im_links = []
src_links = []
img_class = ht_soup.find_all(class_="snaps")
for im in img_class:
    a_tag = im.find("a")
    src = a_tag.attrs['href']
    src_links.append(src)
    img_tag = im.find("img")
    src = img_tag['data-lazy-src']
    im_links.append(src)

# Combining links and headings in indi_l list.
indi_l = []
for h, l ,s in zip(ht_news, im_links,src_links):
    
    indi_l.append((h,l,s))


# Database storing
Data = combine_l + indi_l
for news in Data:
    heading,Image,source=news
    try:
        news = News(heading=heading,image_url=Image,source_url=source )
        news.save()
    except IntegrityError:
        pass

def predict_category():
#     path = os.path.join(settings.MODEL_ROOT, model_name)
    with open('nb_model.pkl', 'rb') as file:
        model = pickle.load(file)  
    for news in Data:
        heading,Image,source=news
        pred = model.predict([heading])
        cat = pre.train.target_names[pred[0]]
        try:
            news = Category(heading=heading,image_url=Image,category=cat )
            news.save()
        except IntegrityError:
            pass

    # pred = model.predict([s])
    # return model.train.target_names[pred[0]]    
predict_category()


# for news in Data:
#     heading,Image,source=news
#     cat = pre.predict_category(heading)
#     try:
#         news = Category(heading=heading,image_url=Image,category=cat )
#         news.save()
#     except IntegrityError:
#         pass





#function for rendering index.html
def index(req):
    return render(req, 'news/index.html', {'indi_l': indi_l, 'combine_l':combine_l})

def landing(req):
    return render(req, 'news/landing.html')

def prediction(req):
    with open('nb_model.pkl', 'rb') as file:
        model = pickle.load(file)  
    if req.method == 'GET':
        data = req.GET.get('data')
        s = data
        cat = ""
        pred = model.predict([data])
        result = pre.train.target_names[pred[0]]
        if result == "rec.sport.baseball" or result == "rec.sport.hockey":
            cat="Sports"
        elif result == 'talk.politics.guns' or result == 'talk.politics.mideast' or  result =='talk.politics.misc':
            cat="Political"
        elif result == "res.auto":
            cat="auto sector "
        elif result == "sci.med":
            cat="Health"
        else:
            cat="others"
    
        return render(req,'news/prediction.html',{'str':cat,'headline':s})
    
def predict(req):
    return render(req,'news/predict.html')

def serach(req):
    return render(req, 'news/serach.html')

def categorey(req):
    return render(req, 'news/categorey.html')
def topnews(req):
    return render(req, 'news/topnews.html',{'combine_l':combine_l})

# list is below is created to combine the both news site image links in news_list.
# new_list = []
# new_list.extend(toi_news)
# new_list.extend(ht_news)
def sports(req):
    spo = Category.objects.all().filter(category__icontains='rec.sport.baseball')
    rts = Category.objects.all().filter(category__icontains='rec.sport.hockey')
    title="Sports"
    return render(req,'news/sports.html',{'data':spo, 'sports':rts,'title':title})

def political(req):
    spo = Category.objects.all().filter(category__icontains='talk.politics.guns')
    rts = Category.objects.all().filter(category__icontains='talk.politics.misc')
    title="Political"
    return render(req,'news/sports.html',{'data':spo, 'sports':rts,'title':title})

def health(req):
    data = Category.objects.all().filter(category__icontains='sci.med')
    title="Health"
    return render(req,'news/sports.html',{'data':data,'title':title })

# def health(req):
#     data = Category.objects.all().filter(category__icontains='rec.autos')
#     title="Auto"
#     return render(req,'news/sports.html',{'data':data,'title':title })
def auto(req):
    data = Category.objects.all().filter(category__icontains='rec.autos')
    title="Auto"
    return render(req,'news/sports.html',{'data':data,'title':title })

def space(req):
    data = Category.objects.all().filter(category__icontains='sci.space')
    title=""
    return render(req,'news/sports.html',{'data':data,'title':title })


def serachbar(req):
     
    if req.method == 'GET':
        search = req.GET.get('search')
        result = News.objects.all().filter(heading__icontains=search)
        message = ""
        return render(req,'news/search.html',{'message': message,'news':result})
        # for i in range(len(new_list)):
        #     if new_list[i] == search :
        #         if i < len(toi_news) and search == toi_news[i] :
        #             message = "News is Founded in scrabed data"
        #             news = new_list[i]
        #             link = m_links[i]
        #             return render(req,'news/search.html',{'message': message, 'news': news, 'link': link})
        #         else:
        #             message = "News is Founded in scrabed data"
        #             news = ht_news[i-len(toi_news)]
        #             link = im_links[i-len(toi_news)]
        #             return render(req,'news/search.html',{'message': message, 'news': news, 'link': link})

          
        message = "Sorry News Not Matches Try Again "
        news = " "
        return render(req,'news/search.html',{'message': message,'news':news})
                

