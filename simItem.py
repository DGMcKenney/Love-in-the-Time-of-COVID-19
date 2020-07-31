#simItem.py
#a class for items in a dating sim
#douglas mckenney

import random

class Item:

    def __init__(self, item, protection, cost):
        self.item = item
        self.protection = protection
        self.cost = cost

    def printInfo(self):
        print("You have a {}.".format(self.item))

    def displayCost(self):
        print("That costs ${}.".format(self.cost))


def makeItem():
    file = "simItems.txt"
    infile = open(file, 'r')
    itemBank = []
    for line in infile:
        itemBank.append(line)
    randomItem = random.choice(itemBank)
    item, protection, cost = randomItem.split("\t")
    return Item(item, protection, cost)

def displayMenu():
    file = "simItems.txt"
    infile = open(file, 'r')
    for line in infile:
        item, protection, cost = line.split("\t")
        print("{}...  ${}".format(item.ljust(13), cost))
        


displayMenu()
item = makeItem()
item.printInfo()
item.displayCost()
