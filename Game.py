'''
The Game.py module is responsible for anything around game logic. The functions in this script handle dice rolling and the use of each roles atributes.
'''

import random
import RogueRole
import EnforcerRole


#Class atributes, these are added to 
firePower = 0
technique = 0
agility = 0
health = 0

'''
updateAtributes changes the atributes based on what roll is selected in App.py when called. This is done in a function so it can be called when its needed
'''
def updateAttributes(roleName):
    global firePower, technique, agility, health

    if roleName.lower() == "rogue": # checks if input is one of the 2 rolls
        #update the empty attributes with the rogues attributes
        print("Rogue selected")
        firePower = RogueRole.rogueFirepower
        technique = RogueRole.rogueTechnique
        agility = RogueRole.rogueAgility
        health = RogueRole.rogueHealth

    else:
        print("Enforcer selected")
        firePower = EnforcerRole.enforcerFirepower
        technique = EnforcerRole.enforcerTechnique
        agility = EnforcerRole.enforcerAgility
        health = EnforcerRole.enforcerHealth


'''
Roll takes 4 parameters;
teckCheck: This is the number that the dice roll must bee higher then to win, successText and Fail Text: print the outcome of success/failure, Attribute: determines the attribute added to the roll
This function handles dice rolling and checking whether that roll is a sucess or a loss 
'''
def Roll(techCheck, successText, failText, attribute):
    global health
    roll = random.randint(1, 20) #Generates a number between 1 and 20
    print("The Dc is ", techCheck) # Displays the number the roll must be greater then.
    print("you rolled", roll, "+", attribute) #Displays the number rolled

    total = roll + attribute #adds roll and attribute
    
    #prints the outcome of success/failure depending on the dice roll 
    if total >= techCheck: 
        print(successText)
    else:
        print(failText)
        health -= 1
