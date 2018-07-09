import os
import sys
import pybel
import openbabel
import re

def findMostSimilar(key,data,found):
    mostSimilarVal = 0
    mostSimilarKey = key
    for k in data:
        sim = 0
        if k != key:
            if set([key,k]) in found:
                sim = found[set([key,k])] | data[key]
            else:
                sim = k | key
                found[set([key,k])] = sim
            if sim > mostSimilarVal:
                mostSimilarVal = sim
                mostSimilarKey = k
    return mostSimilarKey
            

def getDict(csv,dataPath):
    f = open(csv,'r')
    fingerprints = dict()
    for line in f:
        line = line.rstrip("\n")
        line = line.rstrip()
        cols = line.split(" ")
        
        cols[3] = cols[3].rstrip()
        
        ms = pybel.readfile("mol",dataPath+cols[3])
        for m in ms:
            fps = list()
            fp = m.calcfp()
            fps.append(fp)
            fingerprints[cols[3]] = fps[0]     
    return fingerprints

def get1NNPredictionDict(fingerprints):
    #fingerprints = getDict(csv,dataPath)
    newDict = dict()
    found = dict()
    for key in fingerprints:
        newDict[key] = fingerprints[findMostSimilar(key,fingerprints,found)]
    return newDict

def runner(foldPath,dataPath):
    foldPaths = getTrainFiles(foldPath)
    oldDict = dict()
    newDict = dict()
    error = dict()

    for f in foldPaths:
        oldDict[f] = getDict(f,dataPath)
        newDict[f] = get1NNPredictionDict(oldDict)
        error[f] = getRMSE(oldDict[f],newDict[f])
    print(error)
    return error
        
def getRMSE(old,new):
    avgErr = 0
    for key in old:
        rmsd = (old[key]-new[key])**2
        avgErr = avgErr+rmsd
    avgErr = avgErr/len(old)
    return avgErr

def getPaths(foldsPath):
    print(foldsPath)
    paths = list()
    for filename in os.listdir(foldsPath):
        paths.append(foldsPath+filename)
    return paths

def getTrainFiles(foldPath):
    paths = getPaths(foldPath)
    r = re.compile(".*test")
    trainPaths = list(filter(r.match, paths))
    return trainPaths

foldPath = sys.argv[1]
dataPath = sys.argv[2]

runner(foldPath,dataPath)
