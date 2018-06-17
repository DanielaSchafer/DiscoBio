from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
import os
import sys

#puts each fold into a list
def getPaths(path):
    paths = list()
    for filename in os.listdir(path):
        paths.append(filename)
    return paths

def getFingerprintSimilarity(paths, dataPath):
    avgFingerprints = list()
    for(i in range(0,len(paths):
        fp = getAverFingerprint(paths[i], dataPath)
        list.append(fp)
    getSimilarity(avgFingerprints)

#gets average fingerprint for a fold
def getAvgFingerprint(path, dataPath):
    avgFingerprint = 0
    data = open(path,'r')
    size = len(data.readlines())
    data.seek(0)

    for(i in data):
        cols = ran[i].split(',')
        molecules = cols[3]
        fps = [FingerprintMols.FingerprintMol(dataPath+"\\"+x) for x in molecule]
        avgFingerprint= avgFingerprint+fps
    avgFingerprint= avgFingerprint/size
    return avgFingerprint

#prints the similiarity between each fold
def getSimilarity(avgFingerprints):
    for(i in range(0,len(avgFingerprints)-1):
        for(j in range(i+1,len(avgFingerprints))):
            print("Fingerprint Similarity: ",str(i),str(j),DataStructs.FingerprintSimilarity(averageFingerprints[i],averageFingerprints[j]))

def runner(foldsPath,dataPath):
    paths = getPaths(foldsPath)
    getFingerprintSimilarity(paths,dataPath)


#dataPath holds .sdf files
#foldsPath is the path to the folder which contains all the folds
foldsPath =  sys.argv[1]
dataPath = sys.argv[2]
runner(foldsPath,dataPath)
