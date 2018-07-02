import os
import sys

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
                found[set([key,k]) = sim
            if sim > mostSimilarVal:
                mostSimilarVal = sim
                mostSimilarKey = k
    return mostSimilarKey
            

def getDict(csv,dataPath):
    f = open(csv,'r')
    fingerprints = dict()
    for line in f:
        cols = line.split(", ")
        
        cols[0].rstrip()
        cols[1].rstrip()
        cols[2].rstrip()
        if cols[2] != 'nan':
            ms = pybel.readfile("mol",dataPath+cols[0]+"/"+cols[1]+".mol")
            for m in ms:
                fps = list()
                fp = mol.calcfp()
                fps.append(fp)
                fingerprints[cols[0]+"/"+cols[1]] = fps[0]     
    return fingerprints

def get1NNPredictionDict(fingerprints):
    #fingerprints = getDict(csv,dataPath)
    newDict = dict()
    found = dict()
    for key in fingerprints:
        newDict[key] = fingerprints[findMostSimilar(key,fingerprints,found)]
    return newDict

def getNewDictForFolds(foldPath,dataPath):
    foldPaths = getTrainFiles(foldPath)
    oldDict = dict()
    newDict = dict()
    error = dict()

    for f in foldPaths:
        oldDict[f] = getDict(f,dataPath)
        newDict[f] = get1NNPrecitionDict(old)
        error[f] = getRMSE(oldDict[f],newDict[f])
        


        
def getTrainFiles(foldPath):
    paths = getPaths(foldPath)
    r = re.compile(".*test")
    trainPaths = list(filter(r.match, paths))
    return trainPaths

