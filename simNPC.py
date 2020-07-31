#simNPC
#a class for NPCs for a dating sim
#douglas mckenney

from simPerson import *
import random

class NPC(Person):
    def __init__(self, name, status, infectionProb):
        super().__init__(name, status, infectionProb)

    def printInfo(self):
        print("\nNPC name:", self.name, "\nInfection status: ???")

    def getAnswer(self):
        answerIn = random.choice([0,1])
        if answerIn == 1:
            file = "answerBankYes.txt"
            infile = open(file, 'r')
            answerBank = []
            for line in infile:
                answerBank.append(line)
            answerOut = random.choice(answerBank)
            answerOut.strip()
            print('\n\t{}: {}'.format(self.name, answerOut))
        if answerIn == 0:
            file = "answerBankNo.txt"
            infile = open(file, 'r')
            answerBank = []
            for line in infile:
                answerBank.append(line)
            answerOut = random.choice(answerBank)
            answerOut.strip()
            print('\n\t{}: {}'.format(self.name, answerOut))
        return answerIn

def makeNPC():
    #get name
    file = "simNPCs.txt"
    infile = open(file, 'r')
    nameBank = []
    for line in infile:
        nameBank.append(line)
    name = random.choice(nameBank)

    #get status
    status = random.choice(["infected", "uninfected"])

    return NPC(name, status, 0.0)
