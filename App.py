import Game

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
        print("The DC is ", techCheckOne)
        #Calls the Roll function from Game.py, this if statement outputs a diffrent prompt based on Roll's value
        Game.Roll(techCheckOne, "You move Left (SUCC)", "You mess up directions and go right instead (FAIL)")

    #checks if input is option two
    if choice == optionTwo:
        print("The DC is ", techCheckTwo)
        #Calls the Roll function from Game.py, this if statement outputs a diffrent prompt based on Roll's value
        Game.Roll(techCheckTwo,"You move Right (SUCC)", "You mess up directions and go left instead (FAIL)")


ChalCheck("water or something else: ", "Left", 6, "Right", 6)
