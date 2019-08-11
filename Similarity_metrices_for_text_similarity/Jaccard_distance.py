# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 09:40:58 2018

@author: Sumit
"""

base = "Mummy teaches numbers and baby dances"

target = ["Mummy sings Rockabye and baby awakens",
           "Mummy works and baby eats apple",
           "Mummy sings songs and baby dances",
           "Mummy teaches alphabets or baby dances",
           "Mummy sings lullaby and Mummy sleeps",
           "Mummy teaches numbers or baby dances"]
jacardDistanceArray=[]
diceCoefficientArray=[]
def getJaccardDistance(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = 1 - float(len(set1 & set2)) / len(set1 | set2)
    return round(ans, 2)

for i in target:
    jacardDistanceArray.append(getJaccardDistance(base, i))
    diceCoefficientArray.append(getDiceCoefficient(base, i))
    
print("The array for calculated Jaccard Distance")
print(jacardDistanceArray)

def getDiceCoefficient(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = 1 -  2 * float(len(set1 & set2)) / (len(set1) + len(set2))
    return round(ans, 2)

#print("\nFor jaccard: "+str(jd[3])+ " + " +str(jd[4])+ " = " + str(jd[3]+jd[4]))

print("The array for calculated Dice co-efficient")
print(diceCoefficientArray)