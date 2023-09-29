import Game

#Class atributes
global firePower
global technique
global agility
global health

global option1Selected
global option2Selected


'''
ChalCheck takes 5 Parameters;
prompt: the players options, optionOne/optionTwo: the players choices 
techCheckOne/techCheckTwo:The number the players roll must be higher then presented to the player
The function uses these inputs to create prompts then calls on Game.py to do the math if it suceeds or fails
'''
def ChalCheck(prompt, optionOne, techCheckOne, optionTwo, techCheckTwo):
    #presents prompt, choices, and asks for user input
    choice = input(prompt + optionOne + " or " + optionTwo + "? ")
    
    #checks if input is option one
    if choice == optionOne:
        return True

    #checks if input is option two
    elif choice == optionTwo:
        return False


#intro
print("Welcome to Road to Riches! Rules: This is a text based role playing game. You play as one of two bank robbers, you pick where the robbers go and a dice determines your victory.")

#lets user select role
roleChoice = input("Select a role! (Rouge or Enforcer): ")

#selects role based on input
if roleChoice == "Rouge":
    print("Rouge selected")

elif roleChoice == "Enforcer":
    print("Enforcer selected")


if ChalCheck("You approach a door way with a guard near it. will you run or hide ", "Run", 1, "Hide", 1) == True:
    Game.Roll(1, "You sprint past the guard", "You trip and fall")

else:
    Game.Roll(1, "You hide and remain unoticed", "You make some noise")