#simPerson.py
#a class for a person in a dating sim
#douglas mckenney

class Person:
    #constructor
    def __init__(self, name, status, infectionProb):
        #instance variables
        self.name = name.strip()
        self.status = status
        self.infectionProb = infectionProb

    #method(s)

    def getName(self):
        return self.name

    def getStatus(self):
        return self.status

    def changeStatus(self, newStatus):
        self.status = newStatus

    def getInfectionProb(self):
        return self.infectionProb

    def changeInfectionProb(self, newProb):
        self.infectionProb = newProb
