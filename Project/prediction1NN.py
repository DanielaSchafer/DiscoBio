import os
import sys

def findMostSimilar(key,data):


def getDict(csv):
    f = open(csv,'r')
    data = dict()
    for line in f:
        cols = line.split(", ")
        
        cols[0].rstrip()
        cols[1].rstrip()
        cols[2].rstrip()
        if cols[2] != 'nan':
            data[cols[0]+"/"+cols[1]] = cols[2]

    return data


def get1NNPrediction(csv):

