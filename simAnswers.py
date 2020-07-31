#simAnswers.py
#contains functions for giving answers in a dating sim
#douglas mckenney

import random

def getAnswer():
    answerIn = random.choice([0,1])
    if answerIn == 1:
        file = "answerBankYes.txt"
        infile = open(file, 'r')
        answerBank = []
        for line in infile:
            answerBank.append(line)
        answerOut = random.choice(answerBank)
        answerOut.rstrip("\n\n")
        #print("_"*20)
        print('\n\t{}: {}'.format("NPC", answerOut))
        #print("_"*20)
        #print(answerOut)
    if answerIn == 0:
        file = "answerBankNo.txt"
        infile = open(file, 'r')
        answerBank = []
        for line in infile:
            answerBank.append(line)
        answerOut = random.choice(answerBank)
        answerOut.rstrip("\n\n")
        #print("_"*20)
        print('\n\t{}: {}'.format("NPC", answerOut))
        #print("_"*20)
        #print(answerOut)
    return answerIn

#print(answerOut)

if __name__ == "__main__":
    main()
