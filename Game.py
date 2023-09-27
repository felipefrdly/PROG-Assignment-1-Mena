import random

#Roll
def Roll(techCheck, successText, failText):
    roll = random.randint(1, 20)
    print("you rolled", roll)
    if roll >= techCheck:
        print(successText)
    else:
        print(failText)