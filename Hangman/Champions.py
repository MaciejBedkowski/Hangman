def schowTop10():

    listNames = []
    listScore = []

    f = open("TOP10Names.txt")
    for line in f.readlines():
        listNames.append(line.strip())
    f.close()

    f = open("TOP10Score.txt")
    for line in f.readlines():
        listScore.append(line.strip())
    f.close()

    print("Najlepsi gracze:")
    for x in range(len(listNames)):
        print("{x+1}. {listNames[x]}   -   {listScore[x]} pkt.")
