
from rdkit import Chem
import sys
from os import listdir
from rdkit.Chem import AllChem

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
    #print(length)

    counter = 0
    faultyCounter = 0

    for molecules in f:
        if counter !=0:
            cols = molecules.split(',')
            #print(cols[0])
            try:
                suppl = Chem.SDMolSupplier(sdfDataFolder+cols[0])
                for m in suppl:
                    try:
                        atoms = m.GetAtoms()
                        for atom in range(0,len(atoms)):
                            point = m.GetConformer().GetAtomPosition(atom)
                            #print(point)
                            if point.x <minX:
                                minX = point.x
                            elif point.x >maxX:
                                maxX = point.x
                            if point.y <minY:
                                minY = point.y
                            elif point.y >maxY:
                                maxY = point.y
                            if point.z <minZ:
                                minZ = point.z
                            elif point.z >maxZ:
                                maxZ = point.z
                    except:
                        faultyCounter= faultyCounter+1
                        #print("Faulty Molecule "+sdfDataFolder+"/"+cols[0]+" was skipped")
            except:
                faultyCounter = faultyCounter+1
                #print("Faulty Molecule "+sdfDataFolder+"/"+cols[0]+"was skipped")
        counter=counter+1


    x = maxX-minX
    y = maxY-minY
    z = maxZ-minZ
    
    print(str((faultyCounter/counter)*100)+" of files were faulty")
    print(x,y,z)


#dataPath holds .sdf files
#inputPath is file that is used to make folds
dataPath =  sys.argv[1]
inputPath = sys.argv[2]
getDimentions(inputPath,dataPath)
