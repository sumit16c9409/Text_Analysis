# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:01:13 2018

@author: Sumit
"""

import csv
import random
import math
import operator

def loadDataset(filename):
    with open(filename, 'rt') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
    return dataset

  
def subtract_lists(a, b):
    """ Subtracts two lists. Throws ValueError if b contains items not in a """
    # Terminate if b is empty, otherwise remove b[0] from a and recurse
    return a if len(b) == 0 else [a[:i] + subtract_lists(a[i+1:], b[1:]) 
                                  for i in [a.index(b[0])]][0]
    
def split_data(dataset, n):
    random.shuffle(dataset)    
    testset_length = int(len(dataset)/n)    
    test_Set = [dataset[i:i+testset_length] for i in range(0, len(dataset), testset_length)]    
    training_Set=[]
    for i in test_Set:
        training_Set.append(subtract_lists(dataset,i))   
    return {'training_Set':training_Set,'test_Set':test_Set}


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((float(instance1[x]) - float(instance2[x])), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main(k):
    accuracy_list = []
    # prepare data
    dataset = loadDataset('D:\\CSNL\\Text_Analysis\\Assignment6\\xLect6.Progs\\iris.csv')
    splitted_data = split_data(dataset,5)
    trainingSet=splitted_data['training_Set']
    testSet=splitted_data['test_Set']
    # generate predictions
    for i in range(0,len(testSet)):
        trainingSet=splitted_data['training_Set'][i]
        testSet=splitted_data['test_Set'][i]
        predictions=[]
        k = 5
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
        accuracy = getAccuracy(testSet, predictions)
        accuracy_list.append(round(accuracy,2))
    print(accuracy_list)
    return accuracy_list

avr_accuracy_list = []
knn_array = [1, 6, 10, 16, 20 ]
for knn in knn_array:
    accuracy_list =[]
    s = 0
    print("k-fold(From 1 to 5) Accuracy List for knn as "+str(knn)+":")
    accuracy_list = main(knn)
    for i in accuracy_list:
        s = s+i
    print("Average value for k-fold for knn as "+str(knn)+" = " + str(round(s/5,2))+"\n")