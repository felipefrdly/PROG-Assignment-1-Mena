'''
App.py handles all interaction between console and user. It contains the function used to make text prompts letting players choose what they want to do.
'''

import Game
#TODO: put input statements in while loops and break only when people give the 2 options presented

'''
ChalCheck takes 5 Parameters;
prompt: the players options, optionOne/optionTwo: the players choices 
techCheckOne/techCheckTwo:The number the players roll must be higher then presented to the player
The function uses these inputs to create prompts then calls on Game.py to do the math if it suceeds or fails
'''
def ChalCheck(prompt, optionOne, techCheckOne, optionTwo, techCheckTwo):
    #presents prompt, choices, and asks for user input
    while True:
        choice = input(prompt + optionOne + " or " + optionTwo + "? ")
        
        #checks if input is option one, returns true if true
        if choice.lower() == optionOne.lower():
            return True

        #checks if input is option two, returns false if true
        elif choice.lower() == optionTwo.lower():
            return False
        
        else:
            print("Please select on of 2 choices")
            continue


#intro
print("Welcome to Road to Riches! Rules: This is a text based role playing game. You play as one of two bank robbers, you pick where the robbers go and a dice determines your victory.")

#lets user select role
roleChoice = input("Select a role! (Rouge or Enforcer): ")

#changes atributes based on what class is selected 
Game.updateAttributes(roleChoice)

#debug stuff
print(Game.firePower, Game.agility, Game.technique, Game.health)

"""
if ChalCheck("You approach a door way with a guard near it. will you run or hide ", "Run", 1, "Hide", 1) == True:
    Game.Roll(1, "You sprint past the guard", "You trip and fall")

else:
    Game.Roll(1, "You hide and remain unoticed", "You make some noise")
"""

#ChalCheck("You approach a door way with a guard near it. will you run or hide ", "Run", 1, "Hide", 1)