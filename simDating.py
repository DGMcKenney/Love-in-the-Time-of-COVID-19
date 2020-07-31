#Love in the Time of COVID-19
#simDating.py
#a pandemic dating sim game
#douglas mckenney

from simPlayer import *
from simNPC import *
from simVirus import *
from simItem import *
from textwrap import *
import random

def main():
    #display title
    print(("***Love in the Time of COVID-19***").center(70))
    print()
    print(("A dating sim for a plague year.\n").center(70))

    #explain the game
    intro = ("Just because there's a global pandemic going on"
             " doesn't mean that people don't still have emotional"
             " and bodily needs! If you're feeling brave, try dating"
             " to find Love in the Time of COVID-19!")

    wrappedIntro = wrap(intro)
    for line in wrappedIntro:
        print(line.center(80))

    #get player name
    name = input("\nWhat is your name? ")

    #set up and display player
    keepPlaying = "yes"
    player = Player(name, "uninfected", 0.0, 20)
    playerStatus = player.getStatus()
    player.printInfo()
    you = player.getName()

    #shopping
    shopping = input("Do you want to go shopping first? <yes/no>: ")
    while shopping.lower() == 'yes':
        print("What would you like to buy?")
        
    
    #the game
    while True:
        player.changeInfectionProb(0.0)
        #set up virus
        virus = makeVirus()
        species = virus.getSpecies()
        doom = virus.getDeathRate()
        #set up first NPC
        npc = makeNPC()
        npcName = npc.getName()
        status = npc.getStatus()
        if status == "infected":
            infectionRate = virus.getInfectionRate()
            npc.changeInfectionProb(infectionRate)
            species = virus.getSpecies()
            npc.changeStatus(species)
            
        print("\n\n\n\tHey, here comes someone cute!")
        npc.printInfo()

        #ask them out?
        choice = input("\nDo you want to ask them out? <yes/no>: ")

        #no, i don't think i'll ask them out
        if choice.lower() != "yes":
            print('\n\tYeah, I don\'t think they\'re worth the risk...')
            keepPlaying = input("\nDo you want to play again? <yes/no>: ")
            if keepPlaying.lower() == "yes":
                print("\n\tWell, ok...")
                input("\nPress <enter> to continue.")
            elif keepPlaying.lower() != "yes":
                break
            
        #i'm asking them out!        
        if choice.lower() == "yes":
            answer = npc.getAnswer()

            #if they decline
            if answer == 0:
                print('\n\tAh, well- que sera sera.')
                keepPlaying = input("\nDo you want to play again? <yes/no>: ")
                if keepPlaying.lower() == "yes":
                    print("\n\tI love your optimism!")
                    input("\nPress <enter> to continue.")
                elif keepPlaying.lower() != "yes":
                    break

            #if they say yes, go on the date
            if answer == 1:
                player.changeInfectionProb(npc.getInfectionProb())
                print("\n\t*one lovely evening later*")

                #do you want to kiss them?
                choice = input("\nDo you want to try for a kiss? <yes/no> ")

                #i do want to kiss them!
                if choice.lower() == "yes":
                    kiss = random.choice([0,1])
                    print("\n\t*you lean in and...*")

                    #oh, but they don't want to kiss me
                    if kiss == 0:
                        print("\n\tNPC: Oh! Oh. No. No, thank you. ...goodnight.")
                        input("\nPress <enter> to see if you're infected.")
                        outcome = player.infect()
                        gameOver(outcome, player, npcName, species, doom)
                        keepPlaying = input("\nDo you want to play again? <yes/no>: ")
                        if keepPlaying.lower() == "yes":
                            print("\n\tAnother day, another chance to catch a disease!")
                            input("\nPress <enter> to continue.")
                        elif keepPlaying.lower() != "yes":
                            break

                    #kissing achieved!    
                    elif kiss == 1:
                        player.changeInfectionProb(player.getInfectionProb() + (npc.getInfectionProb()/2))
                        print("\n\t*SMOOCH!*")
                        input("\nPress <enter> to see if you're infected.")
                        outcome = player.infect()
                        gameOver(outcome, player, npcName, species, doom)
                        keepPlaying = input("\nDo you want to play again? <yes/no>: ")
                        if keepPlaying.lower() == "yes":
                            print("\n\tYeah, let's keep this roll going!")
                            input("\nPress <enter> to continue.")
                        elif keepPlaying.lower() != "yes":
                            break
                        
                #no kiss, please
                elif choice.lower != "yes":
                    print('\n\tYeah, they WERE coughing a lot during dinner...')
                    input("\nPress <enter> to see if you're infected.")
                    outcome = player.infect()
                    gameOver(outcome, player, npcName, species, doom)
                    keepPlaying = input("\nDo you want to play again? <yes/no>: ")
                    if keepPlaying.lower() == "yes":
                        print("\n\tYeah, don't give up that easily!")
                        input("\nPress <enter> to continue.")
                    elif keepPlaying.lower() != "yes":
                        break
                
    print("\nThat's probably a good choice.")
    print("Sometimes you win by not playing.")

def gameOver(outcome, player, npcName, species, doom):
    player.printInfo()
    if outcome == [0]:
        print("\n\tYou avoided getting sick! High five!")
        print("\n\n\tCongratulations, you acted irresponsibly and suffered no consequences.")
    elif outcome == [1]:
        player = player.changeStatus(species)
        print("\n\tOh damn- you caught {}'s {}.".format(npcName, species))
        print("\tThere is a {}% change you will die.".format(doom*100))
        print("\n\n\tI hope you learned a lesson from all this.")

main()
