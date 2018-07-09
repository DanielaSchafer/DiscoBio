
import openbabel
import pybel
from pybel import*
import sys
from os import listdir


dataPath = 'C:\\Users\\Daniela\\Documents\\discoBio\\FOLDer\\testData.csv'

#gets dimensions of smallest possible box that will fit all molecules
def getDimentions(inputData, sdfDataFolder,outputPath):

    #minX = float('inf')
    maxX =  float('-inf')
    #minY =  float('inf')
    maxY =  float('-inf')
    #minZ =  float('inf')
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
            cols = line.split(", ")
            cols[0].rstrip()
            cols[1].rstrip()
            cols[2].rstrip()
            if cols[2] != 'nan':
                suppl = pybel.readfile("sdf",sdfDataFolder+cols[0]+".sdf")
                for m in suppl:
                    minAX = float('inf')
                    maxAX = float('-inf')
                    minAY = float('inf')
                    maxAY = float('-inf')
                    minAZ = float('inf')
                    maxAZ = float('-inf')
                    
                    for atom in m:
                        point = atom.coords
                        if point[0]<minAX:
                            minAX = point[0]
                        elif point[0]>maxAX:
                            maxAX = point[0]
                        if point[1]<minAY:
                            minAY = point[1]
                        elif point[1] >maxAY:
                            maxAY = point[1]
                        if point[2] <minAZ:
                            minAZ = point[2]
                        elif point[2] >maxAZ:
                            maxAZ = point[2]
                    ax = maxAX-minAX
                    ay = maxAY-minAY
                    az = maxAZ-minAZ
                    if ax>maxX:
                        maxX = ax
                    if ay>maxY:
                        maxY = ay
                    if ax>maxZ:
                        maxZ = az

        counter=counter+1


    x = maxX
    y = maxY
    z = maxZ
    
    with open(outputPath+"dimensions.txt",'w+') as dim:
        dim.writelines("for dataset: "+inputPath+"\n")
        dim.writelines('  x: '+str(x)+' y: '+str(y)+' z: '+str(z))
    print(x,y,z)


#dataPath holds .sdf files
#inputPath is file that is used to make folds
inputPath =  sys.argv[1]
dataPath = sys.argv[2]
outputPath = sys.argv[3]
getDimentions(inputPath,dataPath,outputPath)
