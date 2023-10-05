'''
App.py handles all interaction between console and user. It contains the function used to make text prompts letting players choose what they want to do.
'''

import Game
#TODO: put input statements in while loops and break only when people give the 2 options presented

'''
ChalCheck takes 1 Parameter it creates prompts and lets the user choose one or the other
'''
def ChalCheck(prompt):
    #presents prompt, choices, and asks for user input
    while True: #loops until a
        choice = int(input(prompt))
        
        if choice == 1: #checks if input is option one, returns true if true
            return True

        elif choice == 2: #checks if input is option two, returns false if true
            return False
        
        else:
            print("Please select on of 2 choices")
            continue


#intro
print("""
Rules:
Welcome to Road to Riches! Rules: This is a text based role playing game. You play as one of two bank robbers, you pick where the robbers go and a dice determines your victory.
      
Intro:
You and your crew have been planning this hiest for months. You're in charge of the whole opearation, you call the shots and your henchmen listen. The plan is simple the Rogue
will infiltrate the building, disable security systems, and prepare the escape. The enforcer will move into the bank, calm down the people, collect the money, and escape.
You'll be overseeing this whole operation, lets bring it home.  
""")

roleChoice = input("Select a role! (Rouge or Enforcer): ") #asks the user what input they would like

Game.updateAttributes(roleChoice) #changes atributes based on what class is selected 

'''
This Function combines the Chalcheck function and the Roll function from Game.py to make the gameplay loop,  Chalcheck presents an option and the Roll is changed based on whatever option is chosen
'''
def RogueChallengeOne():
    if ChalCheck("The Rogue arrives at the back of the bank. You see a big steel door with a lock on it, the Rogue stops and sends you a message. 'Doors locked, what should I do?'. <1> Pick the lock <2> Shoot the lock off: ") == True: #checks if option 1 is picked
        Game.Roll(12, "The Rogue moves his hands with finesse, the lock snaps and falls off.", "The Rogue moves the pick into the lock. It gets stuck as he swings the lock around making tons of noise, after enough effort the lock falls off,", Game.agility)

    else: #checks if option 2 is picked
        Game.Roll(12, "The Rouge aims his weapon at the lock, one clean shot and the lock falls off", "The Rogue aims his weapon at the lock, his hand whiffs and he hits the door knob instead making a booming sound. The door opens", Game.firePower)

RogueChallengeOne()



