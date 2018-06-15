import rdkit
from rdkit import Chem
import sys
#from rdkit import Point3D

inputPath = 'C:\\Users\\Daniela\\Documents\\discoBio\\FOLDer\\testData.csv'

m = Chem.MolFromSmiles('C1OC1')

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
        suppl = Chem.SDMolSupplier(cols[0])
        for molecule in suppl:
            m = Chem.MolFromSmiles(molecule)
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
print(minX,maxX,minY,maxY)
