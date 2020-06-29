#Metoda porównuje znak we wszystkich miejscach planszy sprawdzając przy tym czy zapis trzech znaków daje
#zwycięstwo
def IfWin(boardSpace, playerSign):
    if boardSpace[0][0] == playerSign and boardSpace[0][1] == playerSign and boardSpace[0][2] == playerSign:
        return True
    elif boardSpace[1][0] == playerSign and boardSpace[1][1] == playerSign and boardSpace[1][2] == playerSign:
        return True
    elif boardSpace[2][0] == playerSign and boardSpace[2][1] == playerSign and boardSpace[2][2] == playerSign:
        return True
    elif boardSpace[0][0] == playerSign and boardSpace[1][0] == playerSign and boardSpace[2][0] == playerSign:
        return True
    elif boardSpace[0][1] == playerSign and boardSpace[1][1] == playerSign and boardSpace[2][1] == playerSign:
        return True
    elif boardSpace[0][2] == playerSign and boardSpace[1][2] == playerSign and boardSpace[2][2] == playerSign:
        return True
    elif boardSpace[0][0] == playerSign and boardSpace[1][1] == playerSign and boardSpace[2][2] == playerSign:
        return True
    elif boardSpace[0][2] == playerSign and boardSpace[1][1] == playerSign and boardSpace[2][0] == playerSign:
        return True
    else:
        return False