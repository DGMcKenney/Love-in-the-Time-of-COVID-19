#simVirus.py
#a class for a virus in a dating sim
#douglas mckenney

import random

class Virus:

    def __init__(self, family, species, infectionRate, deathRate):
        self.family = family
        self.species = species
        self.infectionRate = float(infectionRate)
        self.deathRate = float(deathRate)

    def printInfo(self):
        print(self.family, self.species, self.infectionRate, self.deathRate)

    def getSpecies(self):
        return self.species
    
    def getInfectionRate(self):
        return self.infectionRate

    def getDeathRate(self):
        return self.deathRate

def makeVirus():
    file = "simViruses.txt"
    infile = open(file, 'r')
    nameBank = []
    for line in infile:
        nameBank.append(line)
    infoStr = random.choice(nameBank)
    family, species, infectionRate, deathRate = infoStr.split("\t")
    return Virus(family, species, infectionRate, deathRate)
