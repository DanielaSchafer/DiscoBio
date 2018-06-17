from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols



def getFingerprtintSimilarity(paths):
    avgFingerprints = list()
    for(i in range(0,len(paths):
        fp = getAverFingerprint(paths[i])
        list.append(fp)
    getSimilarity(avgFingerprints)

def getAvgFingerprint(path):
    avgFingerprint = 0
    data = open("",'r')
    size = len(data.readlines())
    data.seek(0)

    for(i in data):
        cols = ran[i].split(',')
        molecules = cols[0]
        fps = [FingerprintMols.FingerprintMol(x) for x in molecule]
        avgFingerprint= avgFingerprint+fps
    avgFingerprint= avgFingerprint/size
    return avgFingerprint

def getSimilarity(avgFingerprints):
    for(i in range(0,len(avgFingerprints)-1):
        for(j in range(i+1,len(avgFingerprints))):
            print("Fingerprint Similarity: ",str(i),str(j),DataStructs.FingerprintSimilarity(averageFingerprints[i],averageFingerprints[j]))
