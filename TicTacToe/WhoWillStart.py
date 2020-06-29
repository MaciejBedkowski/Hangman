import random

def WhoWillStart(youTurn):
    a = random.randint(0,1)
    if a ==1:
        youTurn = True
    return youTurn