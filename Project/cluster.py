import pybel
import openbabel
import sys
import os

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
        tempLine = m.rstrip("\n")
        tempLine = tempLine.rstrip()
        line  = tempLine

        cols = line.split(", ")
        cols[0].rstrip()
        cols[1].rstrip()
        cols[2].rstrip()
        mol = cols[0]+"/"+cols[1]+" "+cols[2]
        if mol not in isAdded:
            group = list()
            group.append(mol)
            groupID = len(groups)
            newGroup = findAllInGroup(mol,groupID,threshold,group,isAdded,fingerprintHM)
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
          tempLine = line.rstrip("\n")
          tempLine = tempLine.rstrip()
          line = tempLine

          cols = line.split(", ")
          cols[0].rstrip()
          cols[1].rstrip()
          cols[2].rstrip()
          m = pybel.readfile(fileType,dataPath+cols[0]+"/"+cols[1]+"."+fileType)
          for mol in m:
            fps = list()
            fp = mol.calcfp()
            fps.append(fp)
            fingerprints[cols[0]+"/"+cols[1]+" "+cols[2]] = fps
    
          mCounter = mCounter+1
          counter = counter +1

      return fingerprints


def findAllInGroup(m,groupID,threshold,groupMems,isAdded,fingerprintHM):
    neigh = findNeighbors(threshold,m,isAdded,fingerprintHM)
    neigh2 = neigh
    if len(neigh) == 0:
        return neigh

    for n in neigh:
        isAdded[n] = groupID
    for n in neigh2:
        return neigh+findAllInGroup(n,groupID,threshold,groupMems,isAdded,fingerprintHM)

def runner(csvData,dataPath,threshold,fileType,path):
    data = open(csvData,'r')
    fps = getFingerprintHM(csvData,data,fileType)
    isAdded = dict()
    groups = makeClusters(threshold,data,isAdded,fps)
    for i, g in enumerate(groups):
        print("mol in fold "+str(i)+": "+str(len(g)))
        for j,m in enumerate(g):
            cols = m.split(" ")
            groups[i][j] = str(1)+str(cols[1])+" none "+str(cols[0])+".mol "
    
    path = path+'/folds'+str(len(groups))+"/"

    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


    for fold in range(0,len(groups)):
        newTrain = open(path+'train'+str(fold)+'.types','w+')
        newTest = open(path+'test'+str(fold)+'.types','w+')
        newTest.writelines("%s\n" % item for item in groups[fold])
        for f in range(0,len(groups)):
            if(f != fold):
                newTrain.writelines("%s\n" % item for item in groups[f])
        newTrain.close()
        newTest.close()

    print("totalFolds "+str(len(groups)))

csvData = sys.argv[1]
dataPath = sys.argv[2]
threshold = sys.argv[3]
fileType = sys.argv[4]
outputPath = sys.argv[5]

runner(csvData,dataPath,threshold,fileType,outputPath)

