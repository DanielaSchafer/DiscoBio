


def getSecondaryStructureCount(atomList):
    print(len(atomList))
    helical = 0
    sheet = 0
    disordered = 0

    for atoms in atomList:
        if atoms.ss == 'H':
            helical = helical+1
        elif atoms.ss == 'S':
            sheet = sheet+1
        else:
            disordered = disordered+1

    print("there are "+str(helical+sheet)+" atoms that are part of a helix/sheet")
    print("helical % = "+str(float(helical)/float(len(atomList))))
    print("sheet % = "+str(float(sheet)/float(len(atomList))))
    print("disordered % = "+str(float(disordered)/len(atomList)))

def getResidues(atomList):
    residues = 0
    for atoms in list:
        if atom.name == 'CA':
            residues = residues+1



list = cmd.get_model().atom
print(len(list))
getSecondaryStructureCount(list)
