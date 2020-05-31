def WinGame(wordGame,secretPassword):
    if wordGame == secretPassword:
        print("Udało Ci się odkryć hasło!")
        print("Hasło to:")
        print(wordGame)
        input('Press any key')
        return True
    return False