
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm
digits = datasets.load_digits()


# In[6]:


clf = svm.SVC(gamma=0.01,C=100)


# In[7]:


print(len(digits.data))


# In[8]:


x,y= digits.data[:-15],digits.target[:-15]
clf.fit(x,y)


# In[12]:


clf.predict(digits.data[-6].reshape(1,-1))


# In[15]:


plt.imshow(digits.images[-6], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

