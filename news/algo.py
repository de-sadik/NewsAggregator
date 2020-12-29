# %matplotlib inline
import os
import numpy as np
import pickle
# import matplotlib.pyplot as plt
# import seaborn as sns; sns.set()
from sklearn.datasets import fetch_20newsgroups

class Algo:
     def __init__(self):
            self.sting = None
         
            
     def re_me(self,str):
        self.sting=str
        return self.sting
    
    
class Multi:
  def __init__(self):
    self.data = fetch_20newsgroups()
    self.train = None
    self.categories = ['alt.atheism',
    'comp.graphics',
    'comp.os.ms-windows.misc',
    'comp.sys.ibm.pc.hardware',
    'comp.sys.mac.hardware',
    'comp.windows.x',
    'misc.forsale',
    'rec.autos',
    'rec.motorcycles',
    'rec.sport.baseball',
    'rec.sport.hockey',
    'sci.crypt',
    'sci.electronics',
    'sci.med',
    'sci.space',
    'soc.religion.christian',
    'talk.politics.guns',
    'talk.politics.mideast',
    'talk.politics.misc',
    'talk.religion.misc']
    
  def multi_N(self):
      self.train = fetch_20newsgroups(subset='train',categories=self.categories)
      test = fetch_20newsgroups(subset='train',categories=self.categories)
      from sklearn.feature_extraction.text import TfidfVectorizer
      from sklearn.naive_bayes import MultinomialNB
      from sklearn.pipeline import make_pipeline
      #creating a model based on mutinomial naive bayes

      model = make_pipeline(TfidfVectorizer(),MultinomialNB())
        
      clf = model.fit(self.train.data,self.train.target)
      pickle.dump(clf, open("nb_model.pkl", "wb"))
      # path = os.path.join(settings.MODEL_ROOT, model_name)
      # with open(path, 'wb') as file:
      #   pickle.dump(clf, file)
        
      

      # labels = model.predict(test.data)
      # pred = model.predict([s])
      # return train.target_names[pred[0]]



    
    