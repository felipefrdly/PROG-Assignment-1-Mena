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
        print("\n""Rogue selected""\n")
        firePower = RogueRole.rogueFirepower
        technique = RogueRole.rogueTechnique
        agility = RogueRole.rogueAgility
        health = RogueRole.rogueHealth

    else:
        print("\n""Enforcer selected""\n")
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
    print("To pass you must roll a ", techCheck, "or higher!" "\n") # Displays the number the roll must be greater or = then then.
    input("Roll the dice!(Hit Enter!): ""\n") # Asks the user if they would like to roll, if they input anything the code continues
    print("You rolled", roll, "+", attribute, "Skill Bonus!\n") #Displays the number rolled
    total = roll + attribute #adds roll and attribute
    print("Total: ", total)
    
    #Checks if the rolls are 1 or 20, the highest and lowest rolls. If one of those are true it rewards or punishes the plater
    if roll == 1:
        print("Critical Fail!\n")
        health -= 2
    
    elif roll == 20:
        print("Critical Success!\n")
        health += 1

    #prints the outcome of success/failure depending on the dice roll 
    if total >= techCheck: 
        print(successText)
    else:
        print(failText)
        health -= 1
