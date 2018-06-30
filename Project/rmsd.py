import os

def rmsd(energies,expected):
    sum = 0
    for e in range(0,len(energies)):
        sum = sum + ((expected[e]-energies[e])**2)
    return (sum/len(energies))**0.5    


def getEnergies(csv):
    f = open (csv, 'r')
    energies = list()
    for line in f:
        cols = line.split(", ")
        cols[2].rstrip()
        if cols[2] != 'nan':
            energies.append(float(cols[2]))
    return energies

def getMeanEnergy(data):
    sum = 0
    for e in data:
        sum = sum + e
    avg =  sum/len(data)
    
    meanList = list()
    for a in range(0,len(data)):
        meanList.append(avg)
    return meanList

def runner(csv):
    data = getEnergies(csv)
    avgE = getMeanEnergy(data)
    rmsd = rmsd(data,agvE)
    print("avg: "+str(avgE)+" rmsd: "+ str(msd))



csv = argv[1]
runner(csv)
