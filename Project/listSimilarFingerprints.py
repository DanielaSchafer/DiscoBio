import pybel
import openbabel
import datetime
import os
import sys
import re
import time

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
            print(ms)
            output = list()
            fpsList = list()
            for m in ms:    
                fp = m.calcfp()
                fpsList.append(fp)
                if len(fpsList)>0:
                    fingerprints[cols[0]+" "+cols[1]] = fpsList
            counter = counter + 1
            totalCounter = totalCounter+1
        except:
            pass
    return fingerprints

def findMostSimilar(m, fingerprintHM):
    mostSimilarM = 0
    mostSimilarMKey = ''
    for m2 in fingerprintHM:
        sim = fingerprintHM[m] | fingerprint[m2]
        if sim > mostSimilarM:
            mostSimilarM = 0
            mostSimiarMKey = m2
    pairSim = (mostSimilarMKey, mostSimilarM)
    return pairSim
    

def getSimilarityList(csvData,dataPath,foldPath,ouputPath):
    fpsHM = getFingerprintHM(csvData,dataPath,3)
    simHM = dict()
    for m in fpsHM:
        simM = findMostSimilar()
        simHM[m+" "+simM[0]] = simM[1]
    sortedVals = list()
    counter = 0
    for key, value in sorted(simsHM.iteritems(),key=lambda (k,v): (v,k)):
        sortedVals[counter] = ("%s: %s" % (key,value))
    now = datetime.datetime.now()
    with open((foldPath+"similaritylist.txt"),'w+') as newTest:
        newTest.writelines("%s\n" % item for item in sortedVals)

def runner(csvPath,dataPath,outputPath):
    getSimilarityList(csvPath,dataPath,outputPath)

csvPath = sys.argv[2]
dataPath = sys.argv[3]
outputPath = sys.argv[4]

runner(foldPath,csvPath,dataPath,outputPath)

