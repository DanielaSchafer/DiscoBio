
def countHydrogenBonds(atomList):
    hBondTotal = 0
    for atom in range(0,len(atomList)):
        if atomList[atom].symbol == 'O':
            for secondAtom in range(atom,len(atomList)):
                atom1 = atomList[atom].coord
                atom2 = atomList[secondAtom].coord
                dist = distance(atom1[0],atom1[1],atom1[2],atom2[0],atom2[1],atom2[2])
                if dist <= 4 and atomList[secondAtom].symbol == 'N' and atomList[atom].chain != atomList[secondAtom].chain:
                    hBondTotal = hBondTotal+1
                    cmd.distance("bonds", "index "+ str(atomList[atom].index), "index " + str(atomList[secondAtom].index))
        if atomList[atom].symbol == 'N':
            for secondAtom in range(atom,len(atomList)):
                atom1 = atomList[atom].coord
                atom2 = atomList[secondAtom].coord
                dist = distance(atom1[0],atom1[1],atom1[2],atom2[0],atom2[1],atom2[2])
                if dist <= 4 and atomList[secondAtom].symbol == 'O' and atomList[atom].chain != atomList[secondAtom].chain:
                    hBondTotal = hBondTotal+1
                    cmd.distance("bonds","index "+ str(atomList[atom].index), "index " + str(atomList[secondAtom].index))
    print(hBondTotal)


def distance(x,y,z,x2,y2,z2):
    return ((x-x2)**2+(y-y2)**2+(z-z2)**2)**0.5

list = cmd.get_model().atom
#print(len(list))
countHydrogenBonds(list)
