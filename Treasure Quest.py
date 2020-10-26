# Setup
import random
import time

win = ['']
word = ['GOBLIN', 'RICE', 'MOUSE', 'PURPLE', 'VATS', 'MARIO', 'PEACH', 'SAMUS',
            'ORANGE', 'CHOWDER', 'GANON', 'ZELDA', 'ARTHUS', 'DIABLO']

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]

#extra variable
response1 = ["left", "right", "forward", "backward"]
 
# Introduction
print("\n\n\n\n\n\nTREASURE QUEST")
print('....')
time.sleep(1)
print("Make the right choices to find and unlock the Hidden Treasure!")
print('....')
time.sleep(1)
name = input("What is your name, adventurer?\n\n")
print('....')
time.sleep(1)
print("\nGreetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest? yes/no\n\n")
    if response == "yes":
        print('....')
        time.sleep(1)
        print("\nYou head into the forest. You hear crows cawwing in the distance.\n")
        print('....')
        time.sleep(1)
    elif response == "no":
        print('....')
        time.sleep(1)
        print("\nYou are not ready for this quest. Goodbye, " + name + ".")
        print('....')
        time.sleep(1)
        print('-- GAME - OVER --')
        print('....')
        time.sleep(1)
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a bear.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n\n")
    if response == "left":
        print('....')
        time.sleep(1)
        print("\nThe bear eats you. Farewell, " + name + ".")
        print('....')
        time.sleep(1)
        print('-- GAME - OVER --')
        print('....')
        time.sleep(1)
        quit()
    elif response == "right":
        print('....')
        time.sleep(1)
        print("\nYou head deeper into the forest.\n")
        print('....')
        time.sleep(1)
        while response1 not in directions:
            print("To your left, there is a strange noise emmanating from a glowing cave.")
            print("To your right, lies the thickest part of the woods.")
            print("Ahead of you, a fresh breeze coming from an opening in the woods.")
            print("Go back the way you came.\n")
            response1 = input("What direction do you move?\nleft/right/forward/backward\n\n")
            if response1 == "forward":
                print('....')
                time.sleep(1)
                print("\nStumbling through the opening, you accidently snag your foot on a vine and fall to your death! Goodbye " + name + ".")
                print('....')
                time.sleep(1)
                print('-- GAME - OVER --')
                print('....')
                time.sleep(1)
                quit()
            elif response1 == "right":
                print('....')
                time.sleep(1)
                print("\nYou interupt a pack of wolves eating their prey and they eat you. Goodbye " + name + ".")
                print('....')
                time.sleep(1)
                print('-- GAME - OVER --')
                print('....')
                time.sleep(1)
                quit()
            elif response1 == "backward":
                print('....')
                time.sleep(1)
                print("\nThe bear caught your scent and followed you over. He eats you. Goodbye, " + name + ".")
                print('....')
                time.sleep(1)
                print('-- GAME - OVER --')
                print('....')
                time.sleep(1)
                quit()
            elif response1 == "left":
                print('....')
                time.sleep(1)
                print("\nThere, buried under some rocks lies the Treasure!")    #Win

                
                win = input("Enter Password:") ##FIGURE OUT
                if win == word:     
                    print('....')
                    time.sleep(1)
                    print("*************************************************\n--------------------You Win!!!-------------------")
                    print("*************************************************\n")
                    time.sleep(1)
                else:
                    print('....')
                    time.sleep(1)
                    print('-- GAME - OVER --')
                    print('....')
                    time.sleep(1)
                    quit()
                        
                
    elif response == "forward": #additional yes_no for password
        while response not in yes_no:
            print('....')
            time.sleep(1)
            response = input("\nYou scale the wall. Nearing the top, do you decide to hurtle over? yes/no\n\n")
        if response == "yes":
            print('....')
            time.sleep(1)
            print("\nYou make it safely to the other side where a scantily clad fairy gives you a secret password.")
            print('....')
            time.sleep(1)
            y = random.randint(0, 13)

            ##WORK ON!!
            print(word[y])
            print('....')
            time.sleep(1)
            print("Then, a magical door materializes into the stone in front of you, returning you to the other side.\n")
            print('....')
            time.sleep(1)
        elif response == "no":
            print('....')
            time.sleep(1)
            print("You stub your foot on a rock and fall off head first. Goodbye " + name + ".\n")
            print('....')
            time.sleep(1)
            print('-- GAME - OVER --')
            print('....')
            time.sleep(1)
            quit()

        else: 
            print("I didn't understand that.\n")
        
    elif response == "backward":
        print('....')
        time.sleep(1)
        print("\nYou leave the forest. Goodbye, " + name + ".\n")
        print('....')
        time.sleep(1)
        print('-- GAME - OVER --')
        print('....')
        time.sleep(1)
        quit()
    else:
        print("\nI didn't understand that.\n")

##response = ""
##while response not in directions:
##    print("To your left, you see a bear.")
##    print("To your right, there is more forest.")
##    print("There is a rock wall directly in front of you.")
##    print("Behind you is the forest exit.\n")
##    response = input("What direction do you move?\nleft/right/backward\n")
##    if response == "left":
##        print("The bear eats you. Farewell, " + name + ".")
##        quit()
##    elif response == "backward":
##        print("You leave the forest. Goodbye, " + name + ".")
##        quit()
##    elif response == "right":
##        print("You proceed deeper into the forest")
##    else: 
##        print("I didn't understand that.\n")

# you examine the treasure chest and see it is protected by a password and 2 digit number.
#import random.randint
#random.randint [0, 99]


#@py C:\Users\jjmck\AppData\Local\Programs\Python\Python37-32\Treasure Quest.py %*
#@pause


