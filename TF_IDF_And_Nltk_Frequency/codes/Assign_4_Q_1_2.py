# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:23:06 2018

@author: Sumit
"""
import nltk
from nltk.tokenize import TweetTokenizer 
from nltk.corpus import stopwords
tweetTokenizer = TweetTokenizer()
txtFile= open("D:\CSNL\Text_Analysis\Assignment4\Assign_4.txt")
rawText = txtFile.read()
tokenizedText =tweetTokenizer.tokenize(rawText)
my_stop_words = set(stopwords.words('english'))
my_stop_words.update(["$",",","@","*","'","!","[","]","?","©",".",":",'"'])
wordList = [w.lower() for w in tokenizedText if w.lower() not in my_stop_words]
print("The word list After Tokenizaing ",wordList)

from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordList)
finder.apply_freq_filter(3) #Change the frequency here
scored = finder.score_ngrams(bigram_measures.pmi)
print(finder.nbest(bigram_measures.pmi, 10))






