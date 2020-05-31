import random
def RandomPasswordGame(list, wordGame):
    randomNumber = random.randrange(0,len(list))
    wordGame = list[randomNumber]
    return wordGame