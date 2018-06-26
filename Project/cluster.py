import pybel
import openbabel
import sys

def findNeighbors(threshold,m,isAdded,fingerprintHM):
    neigh = list()
    for m2 in fingerprintHM:
        print(m2)
        if m2 in isAdded:
            print("in added")
        else:
            sim = fingerprintHM[m] | fingerprintHM[m2] 
            print(sim)
            if sim < threshold:
                neigh.append(m2)
    print(neigh)
    return neigh

def makeClusters(threshold,molecules, isAdded,fingerprintHM):
    groups = list()
    for m in range(0,len(molecules)):
        tempLine = molecules[m].rstrip("\n")
        tempLine = tempLine.rstrip()
        line  = tempLine
        cols = line.split(" ")
        mol = cols[3]

        if mol in isAdded:
            print("in added")
        else:
            group = list()
            group.append(m)
            groupID = len(groups)
            group = findAllInGroup(m,groupID,threshold,group,isAdded,fingerprintHM)
            groups.append(group)
            for g in group:
                isAdded[g] = groupID
    return groups

def getFingerprintHM(csvData,dataPath):
      data = open(csvData,'r')
      fingerprints = dict()
      mCounter = 0

      for line in data:
          tempLine = line.rstrip("\n")
          tempLine = tempLine.rstrip()
          line = tempLine

          cols = line.split(" ")
          #print(cols)
          #print(dataPath+cols[3])
          ms = pybel.readfile("mol",dataPath+cols[3])
          fpsList = list()
          
          for m in ms:
             fp = m.calcfp()
             fpsList.append(fp)
             fingerprints[cols[3]] = fpsList
    
          mCounter = mCounter+1
      return fingerprints


def findAllInGroup(m,groupID,threshold,groupMems,isAdded,fingerprintHM):
    neigh = findNeighbors(threshold,m,isAdded,fingerprintHM)
    if len(neigh) == 0:
        return groupMems
    for n in neigh:
        groupMems.append(n)
        isAdded[n] = groupID
    for n in neigh:
        findAllInGroup(n,groupID,threshold,groupMems,isAdded,fingerprintHM)

def runner(csvData,dataPath,threshold):
    fps = getFingerprintHM(csvData,dataPath)
    isAdded = dict()
    ms = open(csvData,'r').readlines()
    groups = makeClusters(threshold,ms,isAdded,fps)
    

csvData = sys.argv[1]
dataPath = sys.argv[2]
threshold = sys.argv[3]

runner(csvData,dataPath,threshold)

