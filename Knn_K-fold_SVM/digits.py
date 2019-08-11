# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:07:49 2018

@author: Sumit
"""

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm
digits = datasets.load_digits()


clf = svm.SVC(gamma=0.02, C=100)
print(len(digits.data))


x, y = digits.data[:-15], digits.target[:-15]
clf.fit(x, y)
#d1 = [-1,-4,-5,-9,-10,-15]
print('Prediction:', clf.predict(digits.data[-5].reshape(1,-1)))
plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
#for d in d1:
##    print('Prediction:', classifier.predict(digits.data[d]))
#    plt.imshow(digits.images[d], cmap=plt.cm.gray_r, interpolation='nearest')
#    plt.show()