from rdkit.Chem.Fingerprints import FingerprintMols, MolSimilarity
from rdkit import Chem
import os
import sys
from rdkit import DataStructs
import re


def getFingerprintHM(csvData,dataPath):
    data = open(csvData,'r')
    fingerprints = dict()
    counter = 0
    for line in data:
        cols = line.split(",")
        try:
            #print(dataPath+cols[0])
            ms = Chem.SDMolSupplier(dataPath+cols[0])
            #print(dataPath+cols[0])
            #print(ms)
            fpsList = list()
            for m in ms:
                try:
                    fp = FingerprintMols.FingerprintMol(m)
                    fpsList.append(fp)
                except:
                    print("molecule failed")
                fingerprints[cols[0]] = fpsList
                #print(fingerprints[cols[0]])
                #print(len(fingerprints))
            #print(fpsList)
        except:
            #print(dataPath+cols[0])
            counter = counter + 1
    return fingerprints

def createFoldList(fingerprints, fold):
    foldList = list()
    for fps in fingerprints:
        for fp in fps:
            foldList.append(fp)

def compareFolds(fingerprintHM, fold1, fold2):
    #print(len(fingerprintHM))
    strongestLink = list()
    weakestLink = list()
    for i in range(0,2):
        weakestLink.append("")
        strongestLink.append("")
    
    weakestLinkVal = float('inf');
    strongestLinkVal = float('-inf');

    fold1List = open(fold1,'r')
    fold2List = open(fold2,'r')
    ms = ""
    
    for line in fold1List:
        cols = line.split(" ")
        print(len(fingerprintHM))
        ms = cols[3]
        #print(ms)
        #print(fingerprintHM[ms])
        if ms in fingerprintHM:      
            for line2 in fold2List:
                cols2 = line2.split(" ")
                ms2 = cols2[3]
                #print(ms2)
                if ms2 in fingerprintHM:
                    sim = DataStructs.FingerprintSimilarity(fingerprintHM[ms][0],fingerprintHM[ms2][0])
                    #print("solid file!!")
                    if sim < weakestLinkVal:
                        weakestLinkVal = sim
                        weakestLink[0] = ms
                        weakestLink[1] = ms2
                    if sim > strongestLinkVal:
                        strongestLinkVal = sim
                        strongestLink[0] = ms
                        strongestLink[1] = ms2
                        #except:
                         #   print(line2)

            #except:
             #   print(len(cols))
                #print(fold1)

    print("For partitions: "+ fold1 + " and "+ fold2)
    print("strongest link: " + str(strongestLinkVal) + " between "+str(strongestLink[0]) +" and " +str(strongestLink[1]))
    print("weakest link: "+str(weakestLinkVal)+" between "+str(weakestLink[0])+" and "+str(weakestLink[1]))


def getSimilaritiesBetweenFolds(foldArr,csvData,dataPath,foldPath):
    fpsHM = getFingerprintHM(csvData,dataPath)
    for fold in range(0,len(foldArr)):
        for fold2 in range(fold, len(foldArr)):
            compareFolds(fpsHM,foldPath+foldArr[fold], foldPath+foldArr[fold2])


def getTrainFiles(foldPath):
    paths = getPaths(foldPath)
    r = re.compile(".*train")
    trainPaths = list(filter(r.match, paths))
    return trainPaths
    #print(trainPaths)



def runner(foldPath,csvPath,dataPath):
    trainFiles = getTrainFiles(foldPath)
    getSimilaritiesBetweenFolds(trainFiles,csvPath,dataPath,foldPath)

def getPaths(path):
    paths = list()
    for filename in os.listdir(path):
        paths.append(filename)
    return paths


foldPath = sys.argv[1]
csvPath = sys.argv[2]
dataPath = sys.argv[3]
runner(foldPath,csvPath,dataPath)

