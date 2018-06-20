from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols, MolSimilarity
from rdkit import Chem
from rdkit.ML.Cluster import Murtagh
from rdkit.six.moves import cPickle
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
    for i in range(0,len(paths)):
        fp = getAvgFingerprint(paths[i], dataPath)
        avgFingerprints.append(fp)
    getSimilarity(avgFingerprints)

#gets average fingerprint for a fold
def getAvgFingerprint(path, dataPath):
    avgFingerprint = 0
    data = open(path,'r')
    size = len(data.readlines())
    data.seek(0)
    badFileCounter = 0

    for i in data:
        cols = i.split(' ')
        try:
            molecules = cols[3]
        except:
            print(i)
        try:
            ms = Chem.SDMolSupplier(dataPath+molecules)
            fps = [FingerprintMols.FingerprintMol(x) for x in ms]
            avgFingerprint= avgFingerprint+fps
            print(avgFingerprint)
        except:
            badFileCounter = badFileCounter+1
            #print("invalid file")
    avgFingerprint= avgFingerprint/size
    return avgFingerprint

#prints the similiarity between each fold
def getSimilarity(avgFingerprints):
    for i in range(0,len(avgFingerprints)-1):      
        for j in range(i+1,len(avgFingerprints)):
            print("Fingerprint Similarity: ",str(i),str(j),DataStructs.FingerprintSimilarity(avgFingerprints[i],avgFingerprints[j]))

def runner(foldsPath,dataPath):
    paths = getPaths(foldsPath)

    for file1 in range(0,len(paths)):
        paths[file1] = foldsPath+paths[file1]

    getFingerprintSimilarity(paths,dataPath)


#dataPath holds .sdf files
#foldsPath is the path to the folder which contains all the folds
foldsPath =  sys.argv[1]
dataPath = sys.argv[2]
runner(foldsPath,dataPath)
