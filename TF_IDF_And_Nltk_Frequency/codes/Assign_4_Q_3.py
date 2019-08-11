# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:04:32 2018

@author: Sumit
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:35:52 2018

@author: Sumit
"""
import nltk
import json
import math
from nltk.tokenize import TweetTokenizer 
from nltk.corpus import stopwords


cleaned_spam_list=[]
cleaned_random_list=[]

def readJson(filepath):
    with open(filepath) as data_file:    
        return json.load(data_file)

def data_tokenizing(rawData):
    tokens = nltk.word_tokenize(rawData)
    return tokens

def stop_word_removal(tokenizedText):
    my_stop_words = set(stopwords.words('english'))
    my_stop_words.update(["$",",","@","*","'","!","[","]","?","©",".",":",'"',"%","#"])
    return [w.lower() for w in tokenizedText if w.lower() not in my_stop_words]

spam_list = readJson('D:\\CSNL\\Text_Analysis\\Assignment4\\Spam_tweets.json')
random_list = readJson('D:\\CSNL\\Text_Analysis\\Assignment4\\Random_tweets.json')

def get_entropy(cleaned_lists):
    freqdist = nltk.FreqDist(cleaned_lists)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p * math.log(p,2) for p in probs)

def get_cleaned_list(rawData):
    temp_list =[]
    for documents in rawData:
       after_stop_removal=[] 
       after_stop_removal = stop_word_removal(data_tokenizing(documents))
       temp_list.append(after_stop_removal)
    return temp_list


cleaned_spam_list =get_cleaned_list(spam_list)
cleaned_random_list = get_cleaned_list(random_list)
plain_spam_list =[item for sublist in cleaned_spam_list for item in sublist]
plain_random_list =[item for sublist in cleaned_random_list for item in sublist]
span_random_list = plain_spam_list + plain_random_list


print("Entropy Score for  SPAM tweets  : " + str(get_entropy(plain_spam_list)))
print("Entropy Score for RANDOM tweets  : " + str(get_entropy(plain_random_list)))
print("Entropy Score for Combined tweets  : " + str(get_entropy(span_random_list)))


