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
    while True: #loops until either 1 or 2 is selected
        choice = int(input(prompt))
        
        if choice == 1: #checks if input is option one, returns true if true
            return True

        elif choice == 2: #checks if input is option two, returns false if true
            return False
        
        else:
            print("Please select on of 2 choices")
            continue

'''
All of the Rogue Challenges these functions combine the Chalcheck function and the Roll function from Game.py to make the gameplay loop,  Chalcheck presents an option and the Roll is changed based on whatever option is chosen. All the rogues challenges are the.
'''
def RogueChallengeOne():
    if ChalCheck("The Rogue arrives at the back of the bank. You see a big steel door with a lock on it, the Rogue stops and sends you a message. 'Doors locked, what should I do?'. <1> Pick the lock <2> Shoot the lock off: ") == True: #checks if option 1 is picked
        Game.Roll(22, "The Rogue moves his hands with finesse, the lock snaps and falls off.", "The Rogue moves the pick into the lock. It gets stuck as he swings the lock around making tons of noise, after enough effort the lock falls off.", Game.agility)

    else: #checks if option 2 is picked
        Game.Roll(12, "The Rouge aims his weapon at the lock, one clean shot and the lock falls off.", "The Rogue aims his weapon at the lock, his hand whiffs and he hits the door knob instead making a booming sound. The door opens.", Game.firePower)

def RogueChallengeTwo():
    if ChalCheck("The Rogue makes his way through the building and moves towards the security room. The door requires a keycard to open. The Rogue messages you 'Boss, I can't pick this lock we need to find another way in' Out of his camera feed you spot keycard on a desk and a vent leading to the room. <1> Swipe the card <2> Move through the vent: ") == True: #checks if option 1 is picked
        Game.Roll(22, "The Rogue moves past the table and swipes the card. He moves into the room and towards the computer.", "The Rogue moves past the table and as he moves to swipe it, it falls, people turn but he moves down and grabs the card. He moves into the room and towards the computer ", Game.agility)

    else: #checks if option 2 is picked
        Game.Roll(12, "The Rogue sneaks towards the vent and takes the grate off, sliding in and moving towards the computer.", "The Rogue moves sneaks towards the vent, as he takes the grate off it falls to the floor and bangs, he sprints in before anyone sees and moves towards the computer.", Game.technique)

def RogueChallengeThree():
    if ChalCheck("The Rogue arrives at the security terminal, he has to disable it. As the computer boots up a firewall opens up 'Damn! now what Boss!'. <1> Hack the computer. <2> Shoot the thing!: ") == True: #checks if option 1 is picked
        Game.Roll(22, "The Rogue quickly moves through each security hoop, he makes it to the desktop and turns off security to the vault. he moves towards the exit", "Security is tighter then he thought, he makes it through but triggers some security hoops, the bank knows somethings wrong. he moves towards the exit", Game.technique)

    else: #checks if option 2 is picked
        Game.Roll(12, "The Rogue looks at the computer, aims, and fires! The computer turns off, he moves towards the exit", "The Rogue looks at the computer, aims and fires! It works! a little too well, it starts smoking. he moves towards the exit", Game.firePower)

'''
All of the Enforcer Challenges these functions combine the Chalcheck function and the Roll function from Game.py to make the gameplay loop,  Chalcheck presents an option and the Roll is changed based on whatever option is chosen. All the Enforcer challenges are the.
'''
def EnfoChallengeOne():
    if ChalCheck("The Enforcer moves towards the front of the building. At this point the Rogues done his job now comes the Enforcers job he moves in the bank. The banks packed with people He sends you a message 'Alright Boss, How do I handle this one?'. <1> Talk to the crowd <2> Intimidate the crowd: ") == True: #checks if option 1 is picked
        Game.Roll(22, "The Enforcer gets up on the table and shouts 'Everyone listen up! This is a robbery! Cooperate and it will all go smoothly!' the crowd moves from fear to understanding as they move to the floor. The enforcer moves towards the vault", "The enforcer gets up on the table and shouts 'Everyone listen up! This is a robbery! Cooperate and it will all go smoothly!' the crowd moves from fear to panic as they move to the floor. The enforcer moves towards the vault. Out of the corner of the camera feed you spot people reaching for their phones.")

    else: #checks if option 2 is picked
        Game.Roll(12, "The Enforcer moves towards the middle of the building and fires his weapon up in the air, and shouts 'Get on the floor!'. The crowd quickly hits the floor. The Enforcer moves towards the vault", "The Enforcer moves towards the middle of the building and fires his weapon up in the air but before he can shout some people run away. the rest of the crowd cooperates and the Enforcer moves towards the vault" )

#intro
print("""
Rules:
Welcome to Road to Riches! Rules: This is a text based role playing game. You play as one of two bank robbers, you pick where the robbers go and a dice determines your victory. Each roll can be succeed or failed, your successes and failures change your outcome
      
Intro:
You and your crew have been planning this hiest for months. You're in charge of the whole opearation, you call the shots and your henchmen listen. The plan is simple the Rogue
will infiltrate the building, disable security systems, and prepare the escape. The enforcer will move into the bank, calm down the people, collect the money, and escape.
You'll be overseeing this whole operation with a camera on their glasses, lets bring it home.  
""")

while True: #loops until roleChoice is rogue or enforcer
    roleChoice = input("Select a role! (Rogue or Enforcer): ") #asks the user what input they would like

    if roleChoice.lower() == "rogue":
        break

    elif roleChoice.lower() == "enforcer":
        break

    else:
        print("Please select on of 2 choices")
        continue

Game.updateAttributes(roleChoice) #changes atributes based on what class is selected

#changes what challenges the challenges the player goes through based on the role chosen 
if roleChoice.lower() == "rogue":
    RogueChallengeOne()
    RogueChallengeTwo()
    RogueChallengeThree()

    if Game.health > 0: #if the player wins all 3 challenges they get the win text
        print("The Rogue walks out of the bank and towards the escape van. The coast is clear the rest of the job is the Enforcers hands. You Win!")
    
    else: #if the player wins all 3 challenges they get the lose text
        print("The Rogue walks out of the bank and towards the escape van. The Job was sloppy but it seems like it all went smoothly. As the Rogue gets into the car to wait red and blue lights flash behind him. You Lose!")

else:
    print("run enforcer playthrough")
