1        PROBLEM STATEMENT
 
 The main objectives of this project are to extract the news posted in different news portal sites, organize them in one site and display these news  to the user. The main objectives can be summarized as:
 1.To develop a dynamic news aggregator.
 2.To allow the user to find the latest available news according to different categories.
 3.To provide all news in one place.
 4.To allow users to search news.


2        INTRODUCTION

It is a web application which aggregates data (news articles) from multiple websites. Then presenting the data in one location.News aggregator service is a very important start of the day.There are various publications and news sites online. They publish their content on multiple platforms. Now, imagine when you open 10-20 news sites every day. The time you waste to gain information. Information gain is everything in today’s world.It can give you leverage over those who don’t have it. Now, is there a way we can make it easier? Yes!!.
A news aggregator makes this task easier. In a news aggregator, you can select the websites you want to follow. Then the news aggregator collects the articles for you. And, you are just a click away to get information from various websites.
This aggregator will be capable of retrieving information from news portal websites based on different categories like  title, image, link and so on in future but till date only image and  title factor is considered.  The user is provided with a link of the site that drives them to a specific page where they find the detailed information about the news aggregator.
3        TECHNOLOGY USED
A news aggregator is a combination of web crawlers and web applications. Both of these technologies have their implementation in Python. That makes it easier for us.
So, our news aggregator will work in 3 steps:
It scrapes the web for the articles. (In this Django project, we are scraping a website called indianexpress)
Then it stores the article’s images, links, and title.
The stored objects in the database are served to the client. The client gets information in a nice template.
So, that’s how our web app will work.


4        METHODOLOGY
          there are four modules use for news aggregator as follows:
           1.Home- where user will get all latest news scraped from various news portal
           sites. their user will get links, titles and images related to that news.
2.Refresh- refresh is a feature where users will replace news with the latest news scrap by news aggregator.
3.search-here user can search for different news what he wants to search from news aggregator.
4.categories-where all news are categorised into different genres as the news containing that related news.

4.1     ALGORITHM
The process of feature selection is succeeded by the classification of unseen news into their respective categories.  Classification  algorithms  most commonly  used  for  news  classification  are  Naïve  Bayes.
Multinomial Naïve Bayes
Multinomial  Naïve  Bayes is  a  probabilistic  algorithm  used  in  natural  language  processing problems. In order to predict the category of a given sample, it applies Bayes theorem to calculate the probability of each category. It works on the strong assumption that each feature is independent of the other. News classification using Naïve   Bayes   algorithm is easy   to implement   and   performs satisfactorily. But it shows poor performance when the assumption is violated i.e. when the features are highly correlated.
           Advantages of Naive Bayes Classifier :
It is simple and easy to implement
It doesn’t require as much training data
It handles both continuous and discrete data
It is highly scalable with the number of predictors and data points
It is fast and can be used to make real-time predictions
It is not sensitive to irrelevant features

code:
with open('news', 'r') as f:
    text = f.read()
    news = text.split("\n\n")
    count = {'sport': 0, 'world': 0, "us": 0, "business": 0, "health": 0, "entertainment": 0, "sci_tech": 0}
    for news_item in news:
        lines = news_item.split("\n")
        print(lines[6])
        file_to_write = open('data/' + lines[6] + '/' + str(count[lines[6]]) + '.txt', 'w+')
        count[lines[6]] = count[lines[6]] + 1
        file_to_write.write(news_item)  # python will convert \n to os.linesep
        file_to_write.close()


4.2     SOFTWARE REQUIREMENTS
           1.Python 3.8
           2.HTML/CSS,
3.Django framework	
4.SQLite 	
5.Windows 10 operating system


4.3     LIBRARIES/PACKAGES USED
           You need to have some basics of these libraries:
BeautifulSoup-BeautifulSoup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
requests module-The request  module allows you to send HTTP requests using Python.The HTTP request returns a response object with all the response data (content, encoding, status, etc).
 
 
5      RESULT
         
                                                     



