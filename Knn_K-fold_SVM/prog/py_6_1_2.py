
# coding: utf-8

# In[18]:


from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


# In[19]:


knn = KNeighborsClassifier(n_neighbors=5)


# In[20]:


k_range = [1,6,10,16,20]
k_scores = []


# In[21]:


for k in k_range:
     knn = KNeighborsClassifier(n_neighbors=k)
     scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')   


# In[22]:


k_scores.append(scores.mean())


# In[24]:


print(k_scores[1])


# In[29]:


knn = KNeighborsClassifier()
k_range = [1,6,10,16,20]
k_scores = []
for k in k_range:
     knn = KNeighborsClassifier(n_neighbors=k)
     scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy') 
     k_scores.append(scores.mean())
print(k_scores)


# In[30]:


from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


# In[31]:


# read in the iris data
iris = load_iris()

# create X (features) and y (response)
X = iris.data
y = iris.target


# In[33]:


knn = KNeighborsClassifier()
k_range = [1,6,1,16,20]
k_scores = []
for k in k_range:
     knn = KNeighborsClassifier(n_neighbors=k)
     scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy') 
     k_scores.append(scores.mean())
print(k_scores)


# In[34]:


knn = KNeighborsClassifier()
k_range = [1,6,10,16,20]
k_scores = []
for k in k_range:
     knn = KNeighborsClassifier(n_neighbors=k)
     scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy') 
     k_scores.append(scores.mean())
print(k_scores)


# In[35]:


from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5)


# In[37]:


print(X.len
    )


# In[40]:


print(X.length)


# In[43]:


print(len(X_train))


# In[45]:


knn = KNeighborsClassifier()
k_range = [1,6,10,16,20]
k_scores = []
for k in k_range:
     knn = KNeighborsClassifier(n_neighbors=k)
     scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy') 
     k_scores.append(scores.mean())
print(k_scores)


# In[46]:


split_array =[0.5
for k in k_range:
    for split_val in split_array
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
     knn = KNeighborsClassifier(n_neighbors=k)
     scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy') 
     k_scores.append(scores.mean())
print(k_scores)


# In[47]:


split_array =[0.5,0.90]
for k in k_range:
    for split_val in split_array
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
     knn = KNeighborsClassifier(n_neighbors=k)
     scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy') 
     k_scores.append(scores.mean())
print(k_scores)


# In[49]:


split_array =[0.5,0.90]
for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy') 
         k_scores.append(scores.mean())
print(k_scores)


# In[50]:


from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


# In[51]:


knn = KNeighborsClassifier()


# In[52]:


k_range = [1,6,10,16,20]
k_scores = []


# In[53]:


split_array =[0.5,0.90]


# In[54]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy') 
         k_scores.append(scores.mean())
print(k_scores)


# In[55]:


split_array =[0.5,0.90]


# In[58]:


for split_val in split_array:
     X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
     print(len(y_test))


# In[59]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_test, cv=10, scoring='accuracy') 
         k_scores.append(scores.mean())
print(k_scores)


# In[60]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy') 
         k_scores.append(scores.mean())
print(k_scores)


# In[61]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_scores.append(scores.mean())
print(k_scores)


# In[62]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=20, scoring='accuracy') 
         k_scores.append(scores.mean())
print(k_scores)


# In[63]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_scores.append(scores.mean())
print(k_scores)


# In[64]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn.fit(X_train,y_train)
         y_pred=knn.predict(X_test)
         scores.append(metrics.accuracy_score(y_test,y_pred))
print(k_scores)


# In[65]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


# In[66]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn.fit(X_train,y_train)
         y_pred=knn.predict(X_test)
         scores.append(metrics.accuracy_score(y_test,y_pred))
print(k_scores)


# In[67]:


scores=[]


# In[68]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn.fit(X_train,y_train)
         y_pred=knn.predict(X_test)
         scores.append(metrics.accuracy_score(y_test,y_pred))
print(k_scores)


# In[69]:


split_array =[0.5,0.90]


# In[70]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn.fit(X_train,y_train)
         y_pred=knn.predict(X_test)
         scores.append(metrics.accuracy_score(y_test,y_pred))
print(k_scores)


# In[71]:


split_array =[0.5,0.80]
for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn.fit(X_train,y_train)
         y_pred=knn.predict(X_test)
         scores.append(metrics.accuracy_score(y_test,y_pred))
print(k_scores)


# In[73]:


for k in k_range:
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_scores.append(scores.mean())
print(k_scores)


# In[76]:


K_values_score=[]
for k in k_range:
    k_for_each_split=[]
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_for_each_split.append(scores.mean()*100)
    K_values_score.append(k_for_each_split)
print(K_values_score)


# In[79]:


split_array =[0.33,0.5,0.67,0.80]


# In[81]:


K_values_score=[]
for k in k_range:
    k_for_each_split=[]
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_for_each_split.append(round(scores.mean()*100,2)
    K_values_score.append(k_for_each_split)
print(K_values_score)


# In[82]:


K_values_score=[]
for k in k_range:
    k_for_each_split=[]
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_for_each_split.append(round(scores.mean()*100,2))
    K_values_score.append(k_for_each_split)
print(K_values_score)


# In[83]:


K_values_score=[]
for k in k_range:
    k_for_each_split=[]
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_test, cv=5, scoring='accuracy') 
         k_for_each_split.append(round(scores.mean()*100,2))
    K_values_score.append(k_for_each_split)
print(K_values_score)


# In[84]:


K_values_score=[]
for k in k_range:
    k_for_each_split=[]
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_for_each_split.append(round(scores.mean()*100,2))
    K_values_score.append(k_for_each_split)
print(K_values_score)


# In[85]:


k_range = [10,6,1,16,20]


# In[86]:


K_values_score=[]
for k in k_range:
    k_for_each_split=[]
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_for_each_split.append(round(scores.mean()*100,2))
    K_values_score.append(k_for_each_split)
print(K_values_score)


# In[87]:


K_values_score=[]
for k in k_range:
    k_for_each_split=[]
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_for_each_split.append(round(scores.mean()*100,2))
    K_values_score.append(k_for_each_split)
print(K_values_score)


# In[92]:


avg_scores=[]
for i in K_values_score:
    temp=0
    for j in i:
        temp+=j
    avg_scores.append(temp/4)    
        
print(avg_scores)


# In[93]:


k_range = [1,6,10,16,20]


# In[100]:


K_values_score=[]
for k in k_range:
    k_for_each_split=[]
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_for_each_split.append(round(scores.mean()*100,2))
    K_values_score.append(k_for_each_split)
print(K_values_score)


# In[106]:


avg_scores=[]
for i in K_values_score:
    temp=0
    for j in i:
        temp+=j
    avg_scores.append(temp/4)    
        
print(avg_scores)


# In[102]:


split_array =[0.33,0.5,0.67,0.80]


# In[109]:


k_range = [1,6,10,16,20]


# In[118]:


K_values_score=[]
for k in k_range:
    k_for_each_split=[]
    for split_val in split_array:
         X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=split_val)
         knn = KNeighborsClassifier(n_neighbors=k)
         scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
         k_for_each_split.append(round(scores.mean()*100,2))
    K_values_score.append(k_for_each_split)
print(K_values_score)


# In[119]:


avg_scores=[]
for i in K_values_score:
    temp=0
    for j in i:
        temp+=j
    avg_scores.append(temp/4)    
        
print(avg_scores)


# In[121]:


avg_scores_dict={}
for i in K_values_score:
    temp=0
    for j in i:
        temp+=j
    avg_scores_dict.update("The average score for k ="+k_range[i],temp/4)    


# In[122]:


k_range[i]


# In[123]:


k_range[0]


# In[129]:


avg_scores_dict={}
for i in range(len(K_values_score)):
    temp=0
    for j in range(len(K_values_score[i])):
        temp+=j
    avg_scores_dict.update(k_range[i],temp/4)  


# In[138]:


avg_scores_dict={}
for i in range(len(K_values_score)):
    temp=0
    for j in range(len(K_values_score[i])):
        temp+=K_values_score[i][j]
    avg_scores_dict.update({"The Average value 5 fold for knn = "+k_range[i]+"":temp/4}) 


# In[141]:


print(avg_scores_dict)


# In[147]:


avg_scores_dict={}
for i in range(len(K_values_score)):
    temp=0
    for j in range(len(K_values_score[i])):
        temp+=K_values_score[i][j]
    avg_scores_dict.update({"The Average value of n-fold for knn = "+str(k_range[i])+" is ":temp/4}) 


# In[148]:


for i in avg_scores_dict:
    print(i,avg_scores_dict[i])

