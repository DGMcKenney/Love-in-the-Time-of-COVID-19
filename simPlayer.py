#simPlayer.py
#a class for a player in a dating sim
#douglas mckenney

from simPerson import *
import random

class Player(Person):
    def __init__(self, name, status, infectionProb, money):
        self.money = money
        super().__init__(name, status, infectionProb)

    def printInfo(self):
        print("\nPlayer name:", self.name, "\nInfection status:", self.status, self.money)

    def answer(self):
        answer = input("What is your answer? ")
        return answer

    def infect(self):
        risk = self.getInfectionProb()
        outcome = random.choices([0, 1], weights = [1-risk, risk])
        return outcome
        #random.choice() returns 0 and 1, while random choices returns [0] and [1]

    def buySell(self, price):
        self.money = self.money - price

doug = Player("Douglas", "uninfected", .1, 20)
doug.printInfo()
doug.buySell(10)
doug.printInfo()
