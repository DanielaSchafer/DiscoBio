import rdkit
from rdkit import Chem
import sys
#from rdkit import Point3D

dataPath = 'C:\\Users\\Daniela\\Documents\\discoBio\\FOLDer\\testData.csv'

def getDimentions(inputPath, dataPath):

    minX = float('inf')
    maxX =  float('-inf')
    minY =  float('inf')
    maxY =  float('-inf')
    minZ =  float('inf')
    maxZ =  float('-inf')

    f = open(inputPath,'r')
    arr = f.readlines()
    f.seek(0)
    length = len(arr)
    print(length)

    counter = 0

    for molecules in f:
        if counter !=0:
            cols = molecules.split(',')
            print(cols[0])
            suppl = Chem.SDMolSupplier(dataPath+"\\"+cols[0])
            for m in suppl:
                for atom in m.GetAtoms():
                    point = atom.GetAtomPosition()
                    if point.x <minX:
                        minX = point.x
                    elif point.x >maxX:
                        maxX = point.x
                    if point.y <minY:
                        minY = point.y
                    elif point.y >maxY:
                        maxY = point.y
                    if point.x <minX:
                        minX = point.x
                    elif point.z >maxZ:
                        maxZ = point.z
        counter=counter+1

    x = maxX-minX
    y = maxY-minY
    z = maxZ-minZ

    print(x,y,z)


#dataPath holds .sdf files
#inputPath is file that is used to make folds
dataPath =  sys.argv[1]
inputPath = sys.argv[2]
getDimentions(inputPath,dataPath)
