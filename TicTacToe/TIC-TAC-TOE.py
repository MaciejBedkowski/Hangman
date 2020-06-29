import PrintBoard
import StartMenu
import WhoWillStart
import CheckSign
import IfWin
from os import system

#Zadeklarowanie tablicy tablic, która ma puste miejsca do rysowania pierwszej pustej planszy
boardSpace = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 

#Zadeklarowanie zmiennych 
player1 = "X"           #Zmienna przechowywująca znak pierwszego gracza
player2 = ""          #Zmienna przechowywująca znak drugiego gracza
computer =  ""        #Zmienna przechowywująca znak komputera
youTurn = False         #Zmienna przechowywująca turę gracza
a = 0                   #Zmienna wprowadzania wyboru przez gracza


#Menu startowe. Wybór graczy do gry
StartMenu.StartMenu()

#Walidacja wprowadzanej wartośni
while a !=1 and a !=2:
    try:
        a= int(input("Zdecyduj:"))
    except:
        a = 0

#Przypisanie drugiego gracza do rozgrywki
if a == 1:
   computer ="O" 
else:
    player2 ="O"

#Przypisywanie zaczynającego gracza
youTurn = WhoWillStart.WhoWillStart(youTurn)

#GRA!
while True:
    system('cls')
    #Wyrysowanie planszy
    PrintBoard.PrintBoard(boardSpace)

    #Tura gracza pierwszego
    if youTurn:
        print("** TURA GRACZA 1 **")
        print("Podaj współrzędne gdzie chcesz narysować swój znak:")
        sign=input()
        playerSign = player1
        boardSpace = CheckSign.CheckSign(sign,boardSpace,playerSign) 

        youTurn = False         #Zamiana tury

        if IfWin.IfWin(boardSpace,playerSign):
            #WYGRANA!
            win = 1
            break 

    else:
        #Jeśli graczem drugim jest inny gracz
        if player2 == "O":
            print("** TURA GRACZA 2 **")
            print("Podaj współrzędne gdzie chcesz narysować swój znak:")
            sign=input()
            playerSign = player2
            boardSpace = CheckSign.CheckSign(sign,boardSpace,playerSign) 

            youTurn = True         #Zamiana tury

            if IfWin.IfWin(boardSpace,playerSign):
                #WYGRANA!
                win = 2
                break
                    
        else:
            #Jeśli drugim graczem jest komputer
            print("** TURA KOMPUTERA **")
    if ' ' not in boardSpace[0] and ' ' not in boardSpace[1] and ' ' not in boardSpace[2]:
        win = 0
        break

system('cls')
#Wyrysowanie planszy
PrintBoard.PrintBoard(boardSpace)

if win == 0:
    print("Gra zakończyła się REMISEM!")
elif win == 1:
    print("Gra zakończyła się wzycięstwem gracza pierwszego!")
elif win == 2:
    print("Gra zakończyła się wzycięstwem gracza drugiego!")
input("Press any key")