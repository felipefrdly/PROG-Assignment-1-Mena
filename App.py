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

'''
This Function combines the Chalcheck function and the Roll function from Game.py to make the gameplay loop,  Chalcheck presents an option and the Roll is changed based on whatever option is chosen. All the rouge challenges are the.
'''
def RogueChallengeOne():
    if ChalCheck("The Rogue arrives at the back of the bank. You see a big steel door with a lock on it, the Rogue stops and sends you a message. 'Doors locked, what should I do?'. <1> Pick the lock <2> Shoot the lock off: ") == True: #checks if option 1 is picked
        Game.Roll(12, "The Rogue moves his hands with finesse, the lock snaps and falls off.", "The Rogue moves the pick into the lock. It gets stuck as he swings the lock around making tons of noise, after enough effort the lock falls off.", Game.agility)

    else: #checks if option 2 is picked
        Game.Roll(12, "The Rouge aims his weapon at the lock, one clean shot and the lock falls off.", "The Rogue aims his weapon at the lock, his hand whiffs and he hits the door knob instead making a booming sound. The door opens.", Game.firePower)

def RogueChallengeTwo():
    if ChalCheck("The Rogue makes his way through the building and moves towards the security room. The door requires a keycard to open. The Rogue messages you 'Boss, I can't pick this lock we need to find another way in' Out of his camera feed you spot keycard on a desk and a vent leading to the room. <1> Swipe the card <2> Move through the vent: ") == True: 
        Game.Roll(12, "The Rogue moves past the table and swipes the card. He moves into the room and towards the computer.", "The Rogue moves past the table and as he moves to swipe it, it falls, people turn but he moves down and grabs the card. He moves into the room and towards the computer ", Game.agility)

    else: 
        Game.Roll(12, "The Rogue sneaks towards the vent and takes the grate off, sliding in and moving towards the computer.", "The Rogue moves sneaks towards the vent, as he takes the grate off it falls to the floor and bangs, he sprints in before anyone sees and moves towards the computer.", Game.technique)

def RogueChallengeThree():
    if ChalCheck("The Rogue arrives at the security terminal, he has to disable it. As the computer boots up a firewall opens up 'Damn! now what Boss!'. <1> Hack the computer. <2> Shoot the thing!: "):
        Game.Roll(12, "The Rogue quickly moves through each security hoop, he makes it to the desktop and turns off security to the vault. he moves towards the exit", "Security is tighter then he thought, he makes it through but triggers some security hoops, the bank knows somethings wrong. he moves towards the exit", Game.technique)

    else: #checks if option 2 is picked
        Game.Roll(12, "The Rogue looks at the computer, aims, and fires! The computer turns off, he moves towards the exit", "The Rogue looks at the computer, aims and fires! It works! a little too well, it starts smoking. he moves towards the exit", Game.firePower)

#RogueChallengeOne()
#RogueChallengeTwo()
#RogueChallengeThree()

#intro
print("""
Rules:
Welcome to Road to Riches! Rules: This is a text based role playing game. You play as one of two bank robbers, you pick where the robbers go and a dice determines your victory.
      
Intro:
You and your crew have been planning this hiest for months. You're in charge of the whole opearation, you call the shots and your henchmen listen. The plan is simple the Rogue
will infiltrate the building, disable security systems, and prepare the escape. The enforcer will move into the bank, calm down the people, collect the money, and escape.
You'll be overseeing this whole operation, lets bring it home.  
""")

while True:
    roleChoice = input("Select a role! (Rogue or Enforcer): ") #asks the user what input they would like

    if roleChoice.lower() == "rogue":
        break

    elif roleChoice.lower() == "enforcer":
        break

    else:
        print("Please select on of 2 choices")
        continue

Game.updateAttributes(roleChoice) #changes atributes based on what class is selected

if roleChoice.lower() == "rogue":
    RogueChallengeOne()
    RogueChallengeTwo()
    RogueChallengeThree()

else:
    print("run enforcer playthrough")
