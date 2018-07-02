import os
import sys

def findMostSimilar(key,data,found):
    mostSimilarVal = 0
    mostSimilarKey = key
    for k in data:
        sim = 0
        if set([key,k]) in found:
            sim = found[set([key,k])] | data[key]
        else:
            sim = k | key
            found[set([key,k]) = sim
        if sim > mostSimilarVal:
            mostSimilarVal = sim
            mostSimilarKey = k
    return mostSimilarKey
            

def getDict(csv):
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
    return data


def get1NNPrediction(csv):

