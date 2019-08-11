# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:41:05 2018

@author: Sumit
"""

# Example of kNN implemented from Scratch in Python
# By Jason Brownlee
#http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import csv
import random
import math
import operator

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
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
	
def main(split, arrayForNearestNeighbours):
    # prepare data
    trainingSet=[]
    testSet=[]       
    loadDataset('D:\\CSNL\\Text_Analysis\\Assignment6\\xLect6.Progs\\iris.csv', split, trainingSet, testSet)
    accuracyForK =[]
    for k in arrayForNearestNeighbours:
        # generate predictions
        predictions=[]
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
        accuracyForK.append(getAccuracy(testSet, predictions))
    return accuracyForK

finalAccuracy = []
arrayForNearestNeighbours = [1,6, 10, 16,20]
for split in [0.33,0.50,0.67,0.80]:
    finalAccuracy.append(main(split,arrayForNearestNeighbours))
    
print(finalAccuracy)

import matplotlib.pyplot as plt
plt.plot(arrayForNearestNeighbours, finalAccuracy[0], 'r-')
plt.plot(arrayForNearestNeighbours, finalAccuracy[1], 'g-')
plt.plot(arrayForNearestNeighbours, finalAccuracy[2], 'y-')
plt.plot(arrayForNearestNeighbours, finalAccuracy[3], 'c-')
plt.axis([0, 20, 85, 101])
plt.show()

