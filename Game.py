import random

'''
Roll takes 3 parameters;
teckCheck: This is the number that the dice roll must bee higher then to win, successText and Fail Text: print the outcome of success/failure
'''
def Roll(techCheck, successText, failText):
    #Generates a number between 1 and 20
    roll = random.randint(1, 20)
    print("The Dc is ", techCheck)
    print("you rolled", roll)
    
    #prints the outcome of success/failure
    if roll >= techCheck:
        print(successText)
    else:
        print(failText)