#!/usr/bin/env python
from __future__ import print_function
import pybel
import openbabel
import datetime
import os
import sys
import re
import time
import operator

def getFingerprintHM(csvData,dataPath,fileCol):
    data = open(csvData,'r')
    fingerprints = dict()
    counter = 0
    totalCounter = 0
    
    for line in data:
	tempLine = line.rstrip("\n")
	tempLine = tempLine.rstrip()
	line = tempLine

	cols = line.split(", ")
	cols[0] = cols[0].rstrip()
	cols[1] = cols[1].rstrip()
	try:
	    ms = pybel.readfile("sdf",dataPath+cols[0])
	    output = list()
	    fpsList = list()
	    for m in ms:    
		fp = m.calcfp()
		fpsList.append(fp)
		if len(fpsList)>0:
		    fingerprints[cols[0]] = fpsList
	    counter = counter + 1
	    totalCounter = totalCounter+1
	except:
	    pass
    return fingerprints

def findMostSimilar(m, fingerprintHM):
    mostSimilarM = 0
    mostSimilarMKey = ''
    for m2 in fingerprintHM:
	if m2 != m:
		sim = fingerprintHM[m][0] | fingerprintHM[m2][0]
		if sim >= mostSimilarM:
		    mostSimilarM = sim
		    mostSimilarMKey = m2
    return (mostSimilarMKey,mostSimilarM)
    

def getSimilarityList(csvData,dataPath,ouputPath):
    fpsHM = getFingerprintHM(csvData,dataPath,3)
    simHM = dict()
    for m in fpsHM:
        simM = findMostSimilar(m,fpsHM)
        simHM[m+" "+simM[0]] = simM[1]
    sortedVals = list()
    counter = 0
    sortedVals = sorted(simHM.items(),key=operator.itemgetter(1))
    print(len(sortedVals))
    #print(sortedVals)
    for val in sortedVals:
	print(val)
    with open((outputPath+"similaritylist.txt"),'w+') as newTest:
        newTest.writelines("%s\n" % str(item) for item in sortedVals)

def runner(csvPath,dataPath,outputPath):
    getSimilarityList(csvPath,dataPath,outputPath)

csvPath = sys.argv[1]
dataPath = sys.argv[2]
outputPath = sys.argv[3]

runner(csvPath,dataPath,outputPath)

