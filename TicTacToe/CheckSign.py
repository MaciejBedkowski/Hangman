#Zadeklarowanie tablicy przechowywującej poprawne współrzędne planszy
boardSpaceCorect =["A1","1A","A2","2A","3A","A3","B1","1B","B2","2B","3B","B3","C1","1C","2C","C2","3C","C3"]

def CheckSign(sign,boardSpace,playerSign):

    if sign.upper() in boardSpaceCorect:
        if sign.upper() == "A1" or sign.upper() == "1A":
            boardSpace[0][0] = playerSign 
        elif sign.upper() == "A2" or sign.upper() == "2A":
            boardSpace[0][1] = playerSign
        elif sign.upper() == "A3" or sign.upper() == "A3":
            boardSpace[0][2] = playerSign
        elif sign.upper() == "B1" or sign.upper() == "1B":
            boardSpace[1][0] = playerSign
        elif sign.upper() == "B2" or sign.upper() == "2B":
            boardSpace[1][1] = playerSign
        elif sign.upper() == "B3" or sign.upper() == "3B":
            boardSpace[1][2] = playerSign
        elif sign.upper() == "C1" or sign.upper() == "1C":
            boardSpace[2][0] = playerSign
        elif sign.upper() == "C2" or sign.upper() == "2C":
            boardSpace[2][1] = playerSign
        elif sign.upper() == "C3" or sign.upper() == "3C":
            boardSpace[2][2] = playerSign

    return boardSpace