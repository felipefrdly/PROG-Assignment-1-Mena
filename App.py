'''
App.py handles all interaction between console and user. It contains the function used to make text prompts letting players choose what they want to do.
'''

import Game

'''
ChalCheck takes 1 Parameter it creates prompts and lets the user choose one or the other
'''
def ChalCheck(prompt):
    #presents prompt, choices, and asks for user input
    while True: #loops until either 1 or 2 is selected
        choice = input(prompt)

        if choice == "1": #checks if input is option one, returns true if true
            return True

        elif choice == "2": #checks if input is option two, returns false if true
            return False
        
        else:
            print("Please select on of 2 choices")
            continue

'''
All of the Rogue Challenges these functions combine the Chalcheck function and the Roll function from Game.py to make the gameplay loop,  Chalcheck presents an option and the Roll is changed based on whatever option is chosen.
'''
def RogueChallengeOne():
    if ChalCheck("The Rogue arrives at the back of the bank. You see a big steel door with a lock on it, the Rogue stops and sends you a message. 'Doors locked, what should I do?'\n" "<1> Pick the lock\n" "<2> Shoot the lock off" "\n<1> or <2>: ") == True: #checks if option 1 is picked
        Game.Roll(12, "(PASS) The Rogue moves his hands with finesse, the lock snaps and falls off.", "(FAIL) The Rogue moves the pick into the lock. It gets stuck as he swings the lock around making tons of noise, after enough effort the lock falls off.", Game.agility)

    else: #checks if option 2 is picked
        Game.Roll(12, "(PASS) The Rouge aims his weapon at the lock, one clean shot and the lock falls off.", "(FAIL) The Rogue aims his weapon at the lock, his hand whiffs and he hits the door knob instead making a booming sound. The door opens.", Game.firePower)

def RogueChallengeTwo():
    if ChalCheck("The Rogue makes his way through the building and moves towards the security room. The door requires a keycard to open. The Rogue messages you 'Boss, I can't pick this lock we need to find another way in' Out of his camera feed you spot keycard on a desk and a vent leading to the room.\n" "<1> Swipe the card\n" "<2> Move through the vent" "\n<1> or <2>: ") == True: #checks if option 1 is picked
        Game.Roll(14, "(PASS) The Rogue moves past the table and swipes the card. He moves into the room and towards the computer.", "(FAIL) The Rogue moves past the table and as he moves to swipe it, it falls, people turn but he moves down and grabs the card. He moves into the room and towards the computer ", Game.agility)

    else: #checks if option 2 is picked
        Game.Roll(14, "(PASS) The Rogue sneaks towards the vent and takes the grate off, sliding in and moving towards the computer.", "(FAIL) The Rogue moves sneaks towards the vent, as he takes the grate off it falls to the floor and bangs, he sprints in before anyone sees and moves towards the computer.", Game.technique)

def RogueChallengeThree():
    if ChalCheck("The Rogue arrives at the security terminal, he has to disable it. As the computer boots up a firewall opens up 'Damn! now what Boss!'.\n" "<1> Hack the computer\n" "<2> Shoot the thing" "\n<1> or <2>:  ") == True: #checks if option 1 is picked
        Game.Roll(16, "(PASS) The Rogue quickly moves through each security hoop, he makes it to the desktop and turns off security to the vault. he moves towards the exit", "(FAIL) Security is tighter then he thought, he makes it through but triggers some security hoops, the bank knows somethings wrong. he moves towards the exit", Game.technique)

    else: #checks if option 2 is picked
        Game.Roll(16, "(PASS) The Rogue looks at the computer, aims, and fires! The computer turns off, he moves towards the exit", "(FAIL) The Rogue looks at the computer, aims and fires! It works! a little too well, it starts smoking. he moves towards the exit", Game.firePower)

'''
All of the Enforcer Challenges these functions combine the Chalcheck function and the Roll function from Game.py to make the gameplay loop,  Chalcheck presents an option and the Roll is changed based on whatever option is chosen. All the Enforcer challenges are the.
'''
def EnfoChallengeOne():
    if ChalCheck("The Enforcer moves towards the front of the building. At this point the Rogues done his job now comes the Enforcers job he moves in the bank. The banks packed with people He sends you a message 'Alright Boss, How do I handle this one?'.\n" "<1> Run towards the shutter control.\n" "<2> Intimidate the crowd" "\n<1> or <2>: ") == True: #checks if option 1 is picked
        Game.Roll(12, "(PASS) The Enforcer sprints towards the shutter controls and hits the button! The shutters fall to the floor and the Enforcer shouts 'Nobody move! I'll open the shutters when this is over!' the crowd nods and gets on the floor The Enforcer moves towards the vault", "(FAIL) The Enforcer sprints towards the shutters controls but falls!. As he gets up to hit the button you notice a handful of people have ran away!. The Enforcer shouts 'Nobody move! On the floor now!' the rest of the crowd cooperates. The Enforcer moves towards the vault",Game.agility)

    else: #checks if option 2 is picked
        Game.Roll(12, "(PASS) The Enforcer moves towards the middle of the building and fires his weapon up in the air, and shouts 'Get on the floor!'. The crowd quickly hits the floor. The Enforcer moves towards the vault", "(FAIL) The Enforcer moves towards the middle of the building and fires his weapon up in the air but before he can shout some people run away. the rest of the crowd cooperates and the Enforcer moves towards the vault", Game.firePower)

def EnfoChallengeTwo():
    if ChalCheck("The Enforcer arrives at the vault, the door opens seemlessly. Looks like the Rogue did his job, The Enforcer starts bagging cash, you both notice some safe deposit boxes. The Enforcer sends you a message 'Looks like some extra loot! How do we crack it open!'.\n" "<1> Pick the lock\n" "<2> Shoot it open" "\n<1> or <2>: ") == True: #checks if option 1 is picked
        Game.Roll(14, "(PASS) The Enforcer swiftly picks the lock and starts bagging the loot and makes his way towards the escape van.", "(FAIL) The Enforcer tries to pick the lock but can't seem to crack it. It takes a long time, but the box opens and steals the loot. He makes his way towards the escape van.", Game.technique)

    else: #checks if option 2 is picked
        Game.Roll(14, "(PASS) The Enforcer points his weapon at the box and fires!, the door flies off and the Enforcer starts collecting the loot. He makes his way towards the escape van.", "(FAIL) The Enforcer points his weapon at the box and fires!, but nothing happens. He trys again and again until suddenly the door flies off, that wasted a lot of time.the Enforcer starts collecting the loot. He makes his way towards the escape van", Game.firePower)

def EnfoChallengeThree():
    if ChalCheck("As the Enforcer moves to the van the banks security pops around the corner! He hides behind a wall and send you a message 'We got trouble! What do I do!'.\n" "<1> Run for it!\n" "<2> Fire!" "\n<1> or <2>: ") == True: #checks if option 1 is picked
        Game.Roll(16, "(PASS) The Enforcer runs past the guards before they can catch him. He loads the money into the van and gets in the drivers seat.", "(FAIL) The Enforcer runs into the guards! they all fall to the floor and begin to wrestle. After a few minutes the Enforcer manages to escape!. He loads the money into the van and gets into the drivers seat.", Game.agility)

    else: #checks if option 2 is picked
        Game.Roll(16, "(PASS) The Enforcer fires his weapon and the guards retreat!, he loads the money into the van and gets in the drivers seat.", "(FAIL) The Enforcer fires his weapon but misses! The guards fire back and start a full on shoot out. After a long fight the guards back down. he loads the money into the van and gets in the drivers seat.", Game.firePower)


#intro
print("""
Rules:
Welcome to Road to Riches! Rules: This is a text based role playing game. You play as one of two bank robbers, you pick where the robbers go and a dice determines your victory. Each roll can be succeed or failed, your successes and failures change your outcome. If you fail 3 times you lose!
      
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

#changes what challenges the challenges the player goes through based on the role chosen. the if statements contain the respective challenge functons
if roleChoice.lower() == "rogue":
    RogueChallengeOne()
    RogueChallengeTwo()
    RogueChallengeThree()
    print("")

    if Game.health > 0: #if the player wins all 3 challenges they get the win text
        print("The Rogue walks out of the bank and towards the escape van. The coast is clear the rest of the job is the Enforcers hands. You Win!")
    
    else: #if the player wins all 3 challenges they get the lose text
        print("The Rogue walks out of the bank and towards the escape van. The Job was sloppy but it seems like it all went smoothly. As the Rogue gets into the car to wait red and blue lights flash behind him. You Lose!")

else:
    EnfoChallengeOne()
    EnfoChallengeTwo()
    EnfoChallengeThree()
    print("")
    
    if Game.health > 0: #if the player wins all 3 challenges they get the win text
        print("The Enforcer slams the gas and speeds away with the money. The jobs finished! You Win!")

    else: #if the player wins all 3 challenges they get the lose text
        print("The Enforcer slams the gas but is faced with waves of police cars! The job was sloppy. You Lose!")
