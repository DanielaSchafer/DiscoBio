#Generates random folds for training and testing
#ouputs .types files
#args: datapath, savepath, folds OR folds (uses default datapath and savepath)


import csv
import random
import shutil
import os
import sys
import argparse
from csv import reader
from shutil import copyfile


#path: path of folder with files
#folds: array with folds
#creates train and test .types files for each fold
#test file contains one fold, train file contains the rest
def createFiles(path, folds, makeNewFolder):
    if(makeNewFolder):
        path = path+'\\folds'+str(len(folds))+"\\"

        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    for fold in range(0,len(folds)):
         newTrain = open(path+'train'+str(fold)+'.types','w+')
         newTest = open(path+'test'+str(fold)+'.types','w+')
         newTest.writelines(folds[fold])
         for f in range(0,len(folds)):
             if(f != fold):
                newTrain.writelines(folds[f])
         newTrain.close()
         newTest.close()


#path: path data file
#folds: number of folds
#radomly assigns each line into equal folds
def getFolds(path,folds):

    inputPath = path
    f = open(inputPath,'r')

    ran = f.readlines()
    counter = len(ran)
    random.shuffle(ran)
    f.close()

    foldList = list()

    for pathIndex in range(0,folds):
        arr = list()
        for i in range(int(counter*(float(pathIndex)/float(folds))),int(float(counter)*((pathIndex+1)/folds))):
            cols = ran[i].split(',')
            arr.append(str(1)+str(cols[1])+"none "+str(cols[0])+"\n")
        foldList.append(arr)
    return foldList

#Master method, creates folds and files
#path folder must contain a data file named
def foldRunner(dataPath,savePath,folds):
    hasCorrectParams = True
    if type(dataPath) is int:
        print("dataPath (args1) must be a string")
        hasCorrectParams = False
    if type(savePath) is str == False:
        print("dataPath (args2) must be a string")
    if type(folds) is int == False:
        hasCorrectParams = False
        print("folds (args3) must be an int")

    if hasCorrectParams == True:
        arr = getFolds(dataPath,folds)
        createFiles(savePath,arr,True)


#default path and fold count
dataPath = 'C:\\Users\\Daniela\\Documents\\discoBio\\FOLDer\\testData.csv'
savePath = 'C:\\Users\\Daniela\\Documents\\discoBio\\FOLDer'
folds = 3

if(len(sys.argv) >= 4):
    dataPath =  sys.argv[1]
    savePath = sys.argv[2]
    folds =  int(sys.argv[3])
elif len(sys.argv) == 2:
    folds = int(sys.argv[1])

foldRunner(dataPath,savePath,folds)
