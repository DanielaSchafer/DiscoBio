from rdkit.Chem.Fingerprints import FingerprintMols, MolSimilarity
from rdkit import Chem
import os
import sys
from rdkit import DataStructs
import re


def getFingerprintHM(csvData,dataPath):
    data = open(csvData,'r')
    fingerprints = {}
    for line in data:
        cols = line.split(",")
        try:
            ms = Chem.SDMolSupplier(dataPath+cols[0])
            print(dataPath+cols[0])
            print(ms)
            fpsList = list()
            for m in ms:
                try:
                    fp = FingerprintMols.FingerprintMol(m)
                    fpsList.append(fps)
                except:
                    print("molecule failed")
                fingerprints[cols[0]] = fpsList
            print(fpsList)
        except:
            print("file failed")
    return fingerprints

def createFoldList(fingerprints, fold):
    foldList = list()
    for fps in fingerprints:
        for fp in fps:
            foldList.append(fp)

def compareFolds(fingerprintHM, fold1, fold2):
    weakestLink = list()
    strongestLink = list()
    weakestLinkVal = 0;
    strongestLinkVal = 0;

    fold1List = open(fold1,'r')
    fold2List = open(fold2,'r')

    for line in fold1:
        cols = line.split(",")
        ms = cols[3]
        for line2 in fold2:
            cols2 = line.split(",")
            ms2 = cols2[3]
            sim = DataStructs.FingerprintSimilarity(fingerprintHM[ms][0],fingerprintHM[ms2][0])
            if sim < weakestLinkVal:
                weakestLinkVal = sim
                weakestLink[0] = ms
                weakestLink[1] = ms2
            elif sim > strongestLinkVal:
                strongestLinkVal = sim
                strongestLink[0] = ms
                strongestLink[1] = ms2

    print("strongest link: " + str(strongestLinkVal) + " between "+str(strongestLink[0]) +" and " +str(strongestLink[1]))
    print("weakest link: "+str(weakestLinkVal)+" between "+str(weakestLink[0])+" and "+str(weakestLink[1]))


def getSimilaritiesBetweenFolds(foldArr,csvData,dataPath):
    fpsHM = getFingerprintHM(csvData,dataPath)
    for fold in range(0,len(foldArr)):
        for fold2 in range(fold, len(foldArr)):
            compareFolds(fpsHM,foldArr[fold], foldArr[fold2])


def getTrainFiles(foldPath):
    paths = getPaths(foldPath)
    r = re.compile(".*train")
    trainPaths = list(filter(r.match, paths))
    #print(trainPaths)



def runner(foldPath,csvPath,dataPath):
    trainFiles = getTrainFiles(foldPath)
    getSimilaritiesBetweenFolds(trainFiles,csvPath,dataPath)

def getPaths(path):
    paths = list()
    for filename in os.listdir(path):
        paths.append(filename)
    return paths


foldPath = sys.argv[1]
csvPath = sys.argv[2]
dataPath = sys.argv[3]
runner(foldPath,csvPath,dataPath)
    



        
