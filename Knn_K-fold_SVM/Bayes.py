# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:11:28 2018

@author: Sumit
"""

import nltk
from nltk.corpus import names
import random

def gender_features(word):
    #return {'last_letter': word[-1]}
    #return {'last_two_letters': word[-2:]}
    return {'last_and_first': word[-1]+word[0]}  
# gender_features('Shrek') = {'last_letter': 'k'}

male_names = [(name, 'male') for name in names.words('male.txt')]
female_names = [(name, 'female') for name in names.words('female.txt')]
labeled_names = male_names + female_names
random.shuffle(labeled_names)
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
#entries are    ({'last_letter': 'g'}, 'male')
train_set, test_set = featuresets[500:], featuresets[:500]

classifier = nltk.NaiveBayesClassifier.train(train_set)

ans1 = classifier.classify(gender_features('Brenitta'))
ans2 = classifier.classify(gender_features('Vividha'))
ans3 = classifier.classify(gender_features('Alex'))
ans4 = classifier.classify(gender_features('Rose'))
ans5 = classifier.classify(gender_features('Brian'))

print("Brenitta is:", ans1)
print("Emmy is:", ans2)
print("Alex is:", ans3)
print("Rose is:", ans4)
print("Brian is:", ans5)


classifier.show_most_informative_features(5)
print(nltk.classify.accuracy(classifier, test_set))