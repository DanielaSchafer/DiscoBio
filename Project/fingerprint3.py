import datetime
from rdkit.Chem.Fingerprints import FingerprintMols, MolSimilarity
from rdkit import Chem
import os
import sys
from rdkit import DataStructs
import re
import time
import sys

now = datetime.datetime.now()

def readFoldFile(fold):
    foldList = open(fold,'r').readlines()
    list2 = foldList
    tempLine = ""
    counter = 0
    for line in list2:
        tempLine = line.rstrip("\n")
        tempLine = tempLine.rstrip()
        line = tempLine
        list2[counter] = tempLine
        counter=counter+1
    return list2

def getFingerprintHM(csvData,dataPath,fileCol):
    data = open(csvData,'r')
    fingerprints = dict()
    counter = 0
    totalCounter = 0
    
    for line in data:
        tempLine = line.rstrip("\n")
        tempLine = tempLine.rstrip()
        line = tempLine

        cols = line.split(" ")
        #print(cols)
        try:
            ms = Chem.SDMolSupplier(dataPath+cols[fileCol])
            fpsList = list()
            for m in ms:    
                fp = FingerprintMols.FingerprintMol(m)
                fpsList.append(fp)
                if len(fpsList)>0:
                    #print("AYOOO")
                    fingerprints[cols[fileCol]] = fpsList
        except:
            counter = counter + 1
        totalCounter = totalCounter+1
    #print(len(fingerprints))
    return fingerprints

def createFoldList(fingerprints, fold):
    foldList = list()
    for fps in fingerprints:
        for fp in fps:
            foldList.append(fp)

def compareFolds(fingerprintHM, fold1, fold2):

    strongestLink = list()
    weakestLink = list()
    for i in range(0,2):
        weakestLink.append("")
        strongestLink.append("")
    
    weakestLinkVal = float('inf');
    strongestLinkVal = float('-inf');
    simTotal = 0
    fold1List = readFoldFile(fold1)
    fold2List = readFoldFile(fold2)
    ms = ""
    counter = 0
    valuesAccountedFor = 0
    for line in fold1List:

        print(weakestLinkVal,strongestLinkVal, str((counter/len(fold1List))*100))
        counter = counter+1

        cols = line.split(" ")
        ms = cols[3]
        if ms in fingerprintHM:
            #print("yo")
            for line2 in fold2List:
                cols2 = line2.split(" ")
                ms2 = cols2[3]
                if ms2 in fingerprintHM:
                    sim = DataStructs.FingerprintSimilarity(fingerprintHM[ms][0],fingerprintHM[ms2][0])
                    simTotal = simTotal +sim
                    if sim < weakestLinkVal:
                        weakestLinkVal = sim
                        weakestLink[0] = ms
                        weakestLink[1] = ms2
                    if sim > strongestLinkVal:
                        strongestLinkVal = sim
                        strongestLink[0] = ms
                        strongestLink[1] = ms2
                    valuesAccountedFor = valuesAccountedFor +1
    output = "For partitions: "+ fold1 + " and "+ fold2+"\nAverage Similaraity: "+str(simTotal/valuesAccountedFor)+"\nstrongest link: " + str(strongestLinkVal) + " between "+str(strongestLink[0]) +" and " +str(strongestLink[1])+"\nweakest link: "+str(weakestLinkVal)+" between "+str(weakestLink[0])+" and "+str(weakestLink[1])
    print(output)
    return output


def getSimilaritiesBetweenFolds(foldArr,csvData,dataPath,foldPath,ouputPath):
    fpsHM = getFingerprintHM(csvData,dataPath,3)
    output = list()
    for fold in range(0,len(foldArr)-1):
        for fold2 in range(fold+1, len(foldArr)):
            output.append(compareFolds(fpsHM,foldPath+foldArr[fold], foldPath+foldArr[fold2]))
    
    now = datetime.datetime.now()
    with open((outputPath+"ouput"+str(now.hour)+":"+str(now.minute)+"_"+str(now.day)+"-"+str(now.month)+"-"+str(now.year)),'w+') as newTest:
        newTest.writelines("%s\n" % item for item in output)



def getTrainFiles(foldPath):
    paths = getPaths(foldPath)
    r = re.compile(".*test")
    trainPaths = list(filter(r.match, paths))
    return trainPaths



def runner(foldPath,csvPath,dataPath,outputPath):
    trainFiles = getTrainFiles(foldPath)
    getSimilaritiesBetweenFolds(trainFiles,csvPath,dataPath,foldPath,outputPath)

def getPaths(path):
    paths = list()
    for filename in os.listdir(path):
        paths.append(filename)
    return paths


foldPath = sys.argv[1]
csvPath = sys.argv[2]
dataPath = sys.argv[3]
outputPath = sys.argv[4]
runner(foldPath,csvPath,dataPath,outputPath)

