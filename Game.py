'''
The Game.py module is responsible for anything around game logic. The functions in this script handle dice rolling and the use of each roles atributes.
'''

import random
import RogueRole
import EnforcerRole


#Class atributes
firePower = 0
technique = 0
agility = 0
health = 0

'''
updateAtributes changes the atributes based on what roll is selected in App.py when called. This is done in a function so it can be called when its needed
'''
def updateAttributes(roleName):
    global firePower, technique, agility, health
    if roleName.lower() == "rogue":
        print("Rouge selected")
        firePower = RogueRole.rogueFirepower
        technique = RogueRole.rogueTechnique
        agility = RogueRole.rogueAgility
        health = RogueRole.rogueHealth

    else:
        print("Enforcer selected")


'''
Roll takes 4 parameters;
teckCheck: This is the number that the dice roll must bee higher then to win, successText and Fail Text: print the outcome of success/failure. attribute: the number added to the roll
This function handles dice rolling and checking whether that roll is a sucess or a loss
'''
def Roll(techCheck, successText, failText, attribute):
    #Generates a number between 1 and 20
    roll = random.randint(1, 20)
    
    #Displays the number the roll must be greater then.
    print("The Dc is ", techCheck)

    #Displays the number rolled
    print("you rolled", roll, "+", attribute)

    #adds the attribute to the roll
    total = roll + attribute
    
    #prints the outcome of success/failure depending on the dice roll 
    if roll >= techCheck: 
        print(successText)
    else:
        print(failText)
