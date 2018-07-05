import pybel
import openbabel
import datetime
import os
import sys
import re
import time
import multiprocessing 
from multiprocessing import Pool

now = datetime.datetime.now()

def readFoldFile(fold):
    foldList = open(fold,'r').readlines()
    list2 = foldList
    tempLine = ""
    counter = 0
    for line in list2:
        tempLine = line.rstrip("\n")
        tempLine = tempLine.rstrip()
        line = tempLine
        list2[counter] = tempLine
        counter=counter+1
    return list2




def getFingerprintHM(csvData,dataPath,fileCol):
    data = open(csvData,'r')
    fingerprints = dict()
    counter = 0
    totalCounter = 0
    
    for line in data:
        tempLine = line.rstrip("\n")
        tempLine = tempLine.rstrip()
        line = tempLine

        cols = line.split(", ")
        cols[0] = cols[0].rstrip()
        cols[1] = cols[1].rstrip()
        try:
            ms = pybel.readfile("sdf",dataPath+cols[0])
            print(ms)
            output = list()
            fpsList = list()
            for m in ms:    
                fp = m.calcfp()
                fpsList.append(fp)
                if len(fpsList)>0:
                    fingerprints[cols[0]+" "+cols[1]] = fpsList
            counter = counter + 1
            totalCounter = totalCounter+1
        except:
            pass
    return fingerprints





def createFoldList(fingerprints, fold):
    foldList = list()
    for fps in fingerprints:
        for fp in fps:
            foldList.append(fp)




def compareFolds(fingerprintHM, fold1, fold2):

    strongestLink = list()
    weakestLink = list()
    for i in range(0,2):
        weakestLink.append("")
        strongestLink.append("")
    
    weakestLinkVal = float('inf');
    strongestLinkVal = float('-inf');
    simTotal = 0
    fold1List = readFoldFile(fold1)
    fold2List = readFoldFile(fold2)
    ms = ""
    counter = 0
    #valuesAccountedFor = 0
    extremeVals = [float('inf'),float('-inf'),0,0]


    for line in fold1List:
        print(line)
        #print(str(extremeVals[0])+" "+str(extremeVals[1]),str(int((counter/len(fold1List))*100)))
        counter = counter+1

        cols = line.split(" ")
        ms = cols[3].rstrip("\n")
        ms = ms.rstrip()
        cols[1].rstrip()
        ms = ms+" "+cols[1]
        if ms in fingerprintHM:
            extremeVals = compareToSecondFold(fingerprintHM,ms,fold2List,extremeVals)
                    
    output = "For partitions: "+ fold1 + " and "+ fold2+"\nAverage Similaraity: "+str(float(extremeVals[3])/float(extremeVals[2]))+"\nstrongest link: " + str(extremeVals[1]) +"\nweakest link: "+str(extremeVals[0])+"\n\n"
    print(output)
    return output





def compareToSecondFold(fingerprintHM, ms,fold2List,extremeVals):
    for line2 in fold2List:
                cols2 = line2.split(" ")
                ms2 = cols2[3].rstrip()+" "+cols2[1].rstrip()
                if ms2 in fingerprintHM:
                    sim = fingerprintHM[ms][0] | fingerprintHM[ms2][0]
                    #simTotal = simTotal +sim
                    extremeVals[3] = extremeVals[3]+sim
                    if sim < extremeVals[0]:
                        #weakestLinkVal = sim
                        extremeVals[0] = sim
                        #weakestLink[0] = ms
                        #extremeVals[0][1] = ms
                        #weakestLink[1] = ms2
                        #extremeVals[0][2] = ms2
                    if sim > extremeVals[1]:
                        #strongestLinkVal
                        extremeVals[1] = sim
                        #strongestLink
                        #extremeVals[1][1] = ms
                        #strongestLink
                        #extremeVals[1][2] = ms2
                    #valuesAccountedFor = valuesAccountedFor +1
                    extremeVals[2] = extremeVals[2]+1
    return(extremeVals)






def getSimilaritiesBetweenFolds(foldArr,csvData,dataPath,foldPath,ouputPath):
    fpsHM = getFingerprintHM(csvData,dataPath,3)
    output = list()
    for fold in range(0,len(foldArr)-1):
        for fold2 in range(fold+1, len(foldArr)):
            output.append(compareFolds(fpsHM,foldPath+foldArr[fold], foldPath+foldArr[fold2]))
    
    now = datetime.datetime.now()
    with open((foldPath+"foldSimilaritySDF.txt"),'w+') as newTest:
        newTest.writelines("%s\n" % item for item in output)






def getTrainFiles(foldPath):
    paths = getPaths(foldPath)
    r = re.compile(".*test")
    trainPaths = list(filter(r.match, paths))
    return trainPaths





def runner(foldPath,csvPath,dataPath,outputPath):
    trainFiles = getTrainFiles(foldPath)
    getSimilaritiesBetweenFolds(trainFiles,csvPath,dataPath,foldPath,outputPath)




def getPaths(path):
    paths = list()
    for filename in os.listdir(path):
        paths.append(filename)
    return paths


foldPath = sys.argv[1]
csvPath = sys.argv[2]
dataPath = sys.argv[3]
outputPath = sys.argv[4]

runner(foldPath,csvPath,dataPath,outputPath)

