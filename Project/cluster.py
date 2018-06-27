import pybel
import openbabel
import sys

def findNeighbors(threshold,m,isAdded,fingerprintHM):
    neigh = list()
    for m2 in fingerprintHM:
        if m2 not in isAdded:
            sim = fingerprintHM[m][0] | fingerprintHM[m2][0]
            if float(sim) > float(threshold):
                neigh.append(m2)
    return neigh

def makeClusters(threshold,data, isAdded,fingerprintHM):
    groups = list()
    data.seek(0)

    counter = 0

    for m in data:
        
        if counter > 1000:
            break

        tempLine = m.rstrip("\n")
        tempLine = tempLine.rstrip()
        line  = tempLine

        cols = line.split(", ")
        cols[0].rstrip()
        cols[1].rstrip()
        mol = cols[0]+"/"+cols[1]
        if mol not in isAdded:
            group = list()
            group.append(mol)
            groupID = len(groups)
            newGroup = findAllInGroup(mol,groupID,threshold,group,isAdded,fingerprintHM)
            print(newGroup)
            print("hello")
            groups.append(newGroup)
            for g in newGroup:
                isAdded[g] = groupID
        counter = counter +1
    return groups

def getFingerprintHM(csvData,data,fileType):
      fingerprints = dict()
      mCounter = 0
      
      counter = 0

      for line in data:
          if counter > 1000:
              break
          tempLine = line.rstrip("\n")
          tempLine = tempLine.rstrip()
          line = tempLine

          cols = line.split(", ")
          cols[0].rstrip()
          cols[1].rstrip()
          m = pybel.readfile(fileType,dataPath+cols[0]+"/"+cols[1]+"."+fileType)
          for mol in m:
            fps = list()
            fp = mol.calcfp()
            fps.append(fp)
            fingerprints[cols[0]+"/"+cols[1]] = fps
    
          mCounter = mCounter+1
          counter = counter +1

      return fingerprints


def findAllInGroup(m,groupID,threshold,groupMems,isAdded,fingerprintHM):
    neigh = findNeighbors(threshold,m,isAdded,fingerprintHM)
    neigh2 = neigh
    if len(neigh) == 0:
        print(groupMems)
        return neigh

    for n in neigh:
        print("hello")
        #groupMems.append(n)
        isAdded[n] = groupID
    for n in neigh2:
        print("heh")
        return neigh+findAllInGroup(n,groupID,threshold,groupMems,isAdded,fingerprintHM)

def runner(csvData,dataPath,threshold,fileType):
    data = open(csvData,'r')
    fps = getFingerprintHM(csvData,data,fileType)
    isAdded = dict()
    groups = makeClusters(threshold,data,isAdded,fps)
    print(groups)
    print(len(groups))

csvData = sys.argv[1]
dataPath = sys.argv[2]
threshold = sys.argv[3]
fileType = sys.argv[4]

runner(csvData,dataPath,threshold,fileType)

