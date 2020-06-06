#Importowanie definicji ze składowych
import Passwords        
import RandomPassword
from RandomPassword import RandomPasswordGame
import Intro
import Gallows
import SecredPassword
import Instruction
from os import system
import WinGame
import Menu
import Category
import Champions
import SaveChampions
import Options

#Zmienne
passwords = []          #Zmienna listy przechowywująca hasła do gry   
pkt = 2000              #Zmienna przechowywująca ilość pkt do uzyskania
ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','V','X','Y','Z']
#Zmienna przechowująca alfabet do walidacji wprowadzonych liter
wordGame = ""           #Zmienna przetrzymująca hasło do gry
choiceCategory = None   #Zmienna przechowywująca wybór kategorii
choice = None           #Zmienna przechowująca wybór gracza odnoszący się do gry
choiceInGame = None     #Zbiemma wyboru wewnątrz gry
letterToCheck = ""      #Zmienna wprowadzanej litery do sprawdzenia
letters = []            #Lista przechowująca wybrane litery
wrongDecision = 0       #Zmienna przechowywująca ilość błędnych decyzji
secretPassword =""      #Zmienna przechowująca zakryte hasło do odgadnięcia
checkPassword =""       #Zmienna do wprowadzania zgadywania hasła
tmpPassword =""         #Zmienna do tymczasowego przypisywania hasła
playerName = ""         #Zmienna przechowująca imie gracza

#INTRO
Intro.viewIntro()

#Opcje gry
while True:
    Menu.Menu()
#Walidator opcji wprowadzanej przez użytkownika
    try:
        choice = int(input("Naciśnij klawisz:"))
    except ValueError:
        choice = 5

#Sprawdzanie wyboru użytkownika       
    if choice == 0:
        break

    elif choice == 1:
        Instruction.Instruction()

    elif choice == 3:
        Champions.schowTop10()

    elif choice == 2:
        playerName = input("Podaj imię:")

        #Wybór kategorii
        Category.Category()
        try:
            choiceCategory = int(input("Wybierz kategorię hasła:"))
        except ValueError:
            choiceCategory = 5   
        
        #Zaciągnięcie haseł do gry
        passwords = Passwords.GetPasswords(passwords,choiceCategory)

        #Losowanie hasła do gry
        wordGame = RandomPasswordGame(passwords,wordGame)

        #Zakrywanie hasła gry
        secretPassword = SecredPassword.SecredPassword(wordGame)

        while True:
            if wrongDecision < 6:
                system('cls')
                #Wyświetlanie szubienicy
                Gallows.Gallows(wrongDecision)

                #Wyświetlanie Hasła do odgadnięcia
                print("Hasło do odgadnięcia:")
                print(secretPassword)

                #Wypisane wybrane już litery
                print("Podane już litery:")
                for a in letters: print(a, end=',')

                print(f"Twoje pkt:{pkt}")

                Options.Options()
                #Walidator opcji wprowadzanej przez użytkownika
                try:
                    choiceInGame = int(input("Naciśnij klawisz:"))
                except ValueError:
                    choice = 0

                if choiceInGame == 1:
                    letterToCheck = input("Wprowadź literę:")
                    #Walidacja do wprowadzonej wartości
                    if letterToCheck.upper() in ABC:
                        #Sprawdzenie czy litera była już podana
                        if letterToCheck.upper() in letters:
                            input("Już podawałeś tę literę!")
                            continue

                        #Program właściwy
                        else:
                            #Przypisywanie litery do wybranych już liter
                            letters.append(letterToCheck.upper())

                            #Poprawna litera
                            if letterToCheck.upper() in wordGame:
                                for i in range (0,len(wordGame)):
                                    if letterToCheck.upper() == wordGame[i]:
                                        tmpPassword += letterToCheck.upper()
                                    else:
                                        tmpPassword += secretPassword[i]
                               
                                #Przypisanie nowych liter 
                                secretPassword = tmpPassword

                                #Zresetowanie tymczasowego hasła
                                tmpPassword = ""
                                pkt += 100

                                #Wygrana!
                                if WinGame.WinGame(wordGame,secretPassword):
                                    #Resetowanie wartości
                                    system('cls')
                                    letters = []
                                    wrongDecision = 0
                                    SaveChampions.SaveChampions(pkt,playerName)
                                    Champions.schowTop10()
                                    break
                            else:
                                print("PODAŁEŚ NIEPRAWIDŁOWĄ LITERĘ!")
                                wrongDecision += 1
                                pkt -= 400
                    else:
                        print("Wprowadziłeś nieprawidłowy znak")
                        continue
                elif choiceInGame == 2:
                    checkPassword = input("Podaj słowo, które kryje się za hasłem").upper()

                    #Wygrana!
                    if WinGame.WinGame(wordGame,checkPassword):
                        #Resetowanie wartości
                        system('cls')
                        letters = []
                        wrongDecision = 0
                        pkt += 500
                        SaveChampions.SaveChampions(pkt,playerName)
                        Champions.schowTop10()
                        break
                    else:
                        print("PODAŁEŚ NIEPRAWIDŁOWE HASŁO!")
                        wrongDecision += 1
                        pkt -= 500

            #Koniec gry
            else:
                system('cls')
                Gallows.Gallows(wrongDecision)
                print("OOOOO GAME OVER!!! OOOOO")
                #Resetowanie wartości
                letters = []
                wrongDecision = 0
                input('Press any key')
                break
    else:
        print("Wprowadziłeś błędną wartość!")