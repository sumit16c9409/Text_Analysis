# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:21:17 2018

@author: Sumit
"""

vector_dict = {}
def load_docs():
 doc1 = ('d1','Parliamentary election in 2019 will decide fate of Indian people')
 doc2 = ('d2','The states  decide the Indian Parliamentary election dates for 2019')
 doc3 = ('d3',' Indian Parliamentary election for many states goverment in 2019')
 doc4 = ('d4','Indian states have Parliamentary elections in many slots')
 doc5 = ('d5','states of Up and maharashtra has highest candidates for parliamentary election')
 return [doc1, doc2,doc3,doc4,doc5]

vector_dict = load_docs();


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [vector_dict[0][1], vector_dict[1][1], vector_dict[2][1], vector_dict[3][1], vector_dict[4][1]]

trainingSet1 = ["The Indian Parliamentary election  in 2019  for  many states"]
trainingSet1 = trainingSet1 +docs
trainingSet2 = ["states start preperations early"]
trainingSet2 = trainingSet2 +docs
trainingSet3 = ["Ireland is one of the most beautiful countries'"]
trainingSet3 = trainingSet3 +docs

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix_training_1 = tfidf_vectorizer.fit_transform(trainingSet1)  #finds the tfidf score with normalization
tfidf_matrix_training_2 = tfidf_vectorizer.fit_transform(trainingSet2)
tfidf_matrix_training_3 = tfidf_vectorizer.fit_transform(trainingSet3)

print("cosine scores, q1: ",cosine_similarity(tfidf_matrix_training_1[0:1], tfidf_matrix_training_1)[0])
print("euclidean_distances scores, q1: ",euclidean_distances(tfidf_matrix_training_1[0:1], tfidf_matrix_training_1)[0])

print("cosine scores, q2: ",cosine_similarity(tfidf_matrix_training_2[0:1], tfidf_matrix_training_2)[0])
print("euclidean_distances scores, q2: ",euclidean_distances(tfidf_matrix_training_2[0:1], tfidf_matrix_training_2)[0])

print("cosine scores, q3: ",cosine_similarity(tfidf_matrix_training_3[0:1], tfidf_matrix_training_3)[0])
print("euclidean_distances scores, q3: ",euclidean_distances(tfidf_matrix_training_3[0:1], tfidf_matrix_training_3)[0])