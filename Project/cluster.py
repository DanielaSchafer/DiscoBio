from rdkit import Chem


def findNeighbors(threshold,m,isAdded):
    neigh = list()
    for m2 in molecules:
        if !isAdded.contains(m2):
            sim = DataStructs.FingerprintSimilarity(fingerprintHM[m][0],fingerprintHM[m2][0])             
            if sim < threshold:
                neigh.append(m2)
    return neigh

def makeClusters(threshold,molecules, isAdded):
    groups = list()
    for m in range(0,molecules):
        if !isAdded.contains(m):
            group = list()
            group.append(m)
            group = findAllInGroup(m,group)
            groups.append(group)

def getFingerprintHM(csvData,dataPath):
      data = open(csvData,'r')
      fingerprints = {}
      mCounter = 0
      for line in data:
          cols = line.split(",")
          try:
              ms = Chem.SDMolSupplier(dataPath+cols[0])
              fpsList = list()
              for m in ms:
                  try:
                      fp = FingerprintMols.FingerprintMol(m)
                      fpsList.append(fps)
                  except:
                      print("molecule failed")
                  fingerprints[mCounter] = fpsList
          except:
              print("file failed")
      mCounter = mCounter+1
      return fingerprints


def findAllInGroup(m,groupID,threshold,groupMems,isAdded):
    neigh = findNeighbors(m)
    if len(neigh) == 0
        return groupMems
    for n in neigh:
        groupMems.append(n)
        isAdded[n] = groupID
    for n in neigh:
        findAllInGroup(n,threshold,groupMems)

def runner(csvData,dataPath,threshold):
    fps = getFingerprintHM(csvData,dataPath)
    isAdded = {}
    ms = open(csvData,'r').readlines()

    makeClusters(threshold,ms,isAdded)
