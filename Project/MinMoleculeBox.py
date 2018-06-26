
import openbabel
import pybel
from pybel import*
import sys
from os import listdir


dataPath = 'C:\\Users\\Daniela\\Documents\\discoBio\\FOLDer\\testData.csv'

#gets dimensions of smallest possible box that will fit all molecules
def getDimentions(inputData, sdfDataFolder):

    minX = float('inf')
    maxX =  float('-inf')
    minY =  float('inf')
    maxY =  float('-inf')
    minZ =  float('inf')
    maxZ =  float('-inf')
    
    #print(inputData)
    f = open(inputData,'r')
    length = len(f.readlines())
    f.seek(0)

    counter = 0
    faultyCounter = 0

    for molecules in f:
        if counter !=0:
            tempLine = molecules.rstrip("\n")
            tempLine = tempLine.rstrip()
            line  = tempLine
            cols = line.split(" ")
    
            suppl = pybel.readfile("mol",sdfDataFolder+cols[3])
            for m in suppl:
                for atom in m:
                    point = atom.coords
                    if point[0]<minX:
                        minX = point[0]
                    elif point[0]  >maxX:
                        maxX = point[0]
                    if point[1] <minY:
                        minY = point[1]
                    elif point[1] >maxY:
                        maxY = point[1]
                    if point[2] <minZ:
                        minZ = point[2]
                    elif point[2] >maxZ:
                        maxZ = point[2]
        counter=counter+1


    x = maxX-minX
    y = maxY-minY
    z = maxZ-minZ
    
    print(x,y,z)


#dataPath holds .sdf files
#inputPath is file that is used to make folds
inputPath =  sys.argv[1]
dataPath = sys.argv[2]
getDimentions(inputPath,dataPath)
