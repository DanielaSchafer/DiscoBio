#!/usr/bin/env/python
from __future__ import print_function
import pybel
import openbabel
import datetime
import os
import sys
import re

def makeHM(csvData):
    data = open(csvData, 'r')
    energies = dict()

    for line in data:
        tempLine = line.rstrip("\n")
        tempLine = tempLine.rstrip()
        line = tempLine
 
        cols = line.split(", ")
        cols[0] = cols[0].rstrip()
        cols[1] = cols[1].rstrip()
        energies[cols[0]] = float(cols[1])
    return energies

def getFiles(simfile)
    data = open(simfile, 'r')
    pairHM = dict()

    for line in data:
        r = re.compile("dsgdb9nsd_\d.sdf")
        p = re.compile("\d\.\d")
        sim = filter(p.match,line)
        files = list(filter(r.match,line))
        pairHM[files] = sim

def createFile(energies, pairHM,outputPath):
    newlines = list()
    for pair in pairHM:
        a = pair[0]
        b = pair[1]
        sim = pairHM[pair]
        energyA = energies[a]
        energyB = energies[b]
        diff = abs(energyA-energyB)
        string = a+" " +energyA+", "b+" "+energyB+", "+"diff "+diff+" sim "+sim
        newlines.append(string)
        print(string)
    with open((outputPath+"energyDiffSim.txt"),'w+') as newFile:
        newFile.writelines("%s\n" % item for item in newlines)

def runner(csvPath,simPath,outputPath):
    hm = makeHM(csvPath)
    sim = getFiles(simPath)
    createFile(hm,sim)

csvPath = sys.argv[1]
dataPath = sys.argv[2]
outputPath = sys.argv[3]

runner(csvPath,dataPath,outputPath)
