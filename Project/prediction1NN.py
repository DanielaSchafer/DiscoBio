#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import pybel
import openbabel
import re

def findMostSimilar(key,data,found):
    mostSimilarVal = float('inf')
    mostSimilarKey = key
    for k in data:
        sim = float('inf')
        if k != key:
            if (key+k) in found:
                sim = found[(key+k)]
	    elif (k+key) in found:
		sim = found[(k+key)]
            else:
                sim = abs(data[key]-data[k])
		found[(k+key)] = sim
            if sim < mostSimilarVal:
                mostSimilarVal = sim
                mostSimilarKey = k
    return mostSimilarKey
            

def getDict(csv,dataPath):
    f = open(csv,'r')
    fingerprints = dict()
    counter = 0
    for line in f:
	line = line.rstrip("\n")
	line = line.rstrip()
	cols = line.split(" ")
	
	cols[3] = cols[3].rstrip()
	fingerprints[cols[3]] = float(cols[1].rstrip()) 
	counter=counter+1    
    return fingerprints

def get1NNPredictionDict(fingerprints):
    #fingerprints = getDict(csv,dataPath)
    
    print(len(fingerprints))
    newDict = dict()
    found = dict()
    for key in fingerprints:
	#print(len(fingerprints))
        newDict[key] = fingerprints[findMostSimilar(key,fingerprints,found)]
	#print(key)
    return newDict

def runner(foldPath,dataPath,outputPath):
    print("hello")
    foldPaths = getTrainFiles(foldPath) 
    print(foldPaths)
    oldDict = dict()
    newDict = dict()
    error = dict()

    for f in foldPaths:
        oldDict[f] = getDict(f,dataPath)
	print("inputted data into dictionary")
        newDict[f] = get1NNPredictionDict(oldDict[f])
	print("getting prediction values")
        error[f] = getRMSE(oldDict[f],newDict[f])
	print("error calculated")
	print(error[f])
    with open(outputPath+"1NN_predictions.txt", 'w+') as pred:
	pred.writelines(error)
	pred.writelines(error)
    print(error)
        
def getRMSE(old,new):
    avgErr = 0
    for key in old:
        print(key)
	print(len(old), len(new))
	rmsd = (old[key]-new[key])**2
        avgErr = avgErr+rmsd
    avgErr = avgErr/len(old)
    return avgErr

def getPaths(foldsPath):
    print(foldsPath)
    paths = list()
    for filename in os.listdir(foldsPath):
        paths.append(filename)
    print(paths)
    return paths

def getTrainFiles(foldPath):
    paths = getPaths(foldPath)
    r = re.compile("\S{0,}train\d.types\Z")
    trainPaths = list(filter(r.match, paths))
    print(trainPaths)
    return trainPaths

foldPath = sys.argv[1]
dataPath = sys.argv[2]
outputPath = sys.argv[3]

runner(foldPath,dataPath,outputPath)
