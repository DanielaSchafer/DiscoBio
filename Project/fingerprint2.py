from rdkit import DataStructs
import re


def getFingerprintHM(csvData):
    data = open(dsvData,'r')
    fingerprints = {}
    for line in data:
        cols = line.split(",")
        ms = Chem.SDMolSupplier(dataPath+cols[0])
        fps = FingerprintMols.FingerprintMol(ms)
        fingerprints[cols[0]] = fps
        print(fps)
    return fingerprints

def compareFolds(fingerprintHM, fold1, fold2):
    weakesetLink = list()
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
            sim = DataStructs.FingerprintSimilarity(fingerprintHM[ms],fingerprintHM[ms2])
            if sim < weakestLinkVal:
                weakestLinkVal = sim
                weakestLink[0] = ms
                weakestLink[1] = ms2
            elif sim > strongestLinkVal:
                strongestLinkVal = sim
                strongestLink[0] = ms
                strongestLink[1] = ms2

    print("strongest link: " + str(strongestLinkVal) + " between "+str(strongestLink[0]) +" and " +str(strongestLink[1])
    print("weakest link: "+str(weakestLinkVal)+" between "+str(weakestLink[0])+" and "str(weakestLInk[1])


def getSimilaritiesBetweenFolds(foldArr,csvData):
    fpsHM = getFingerprintHM(csvData)
    for fold in range(0,len(foldArr)):
        for fold2 in range(fold, len(foldArr)):
            compareFolds(fpsHM,foldArr[fold], foldArr[fold2])


def getTrainFiles(foldPath):
    paths = getPaths(foldsPath)
    r = re.compile(".*train")
    trainPaths = list(filter(r.match, paths))
    print(trainPaths)



def runnter(foldPath,csvPath):
    trainFiles = getTrainFiles(foldPath)
    getSimilaritiesBetweenFolds(trainFiles,csvPath)



foldPath = sys.argv[1]
csvPath = sys.argv[2]
runner(foldPath,csvPath)
    



        
