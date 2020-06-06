def SaveChampions(pkt, playerName):

    listNames = []
    listScore = []
    flag = True

    f = open("TOP10Names.txt")
    for line in f.readlines():
        listNames.append(line.strip())
    f.close()

    f = open("TOP10Score.txt")
    for line in f.readlines():
        listScore.append(line.strip())
    f.close()

    if len(listNames) == 9:
        for x in range(len(listNames)):
            if int(pkt) > int(listScore[x]):
                listScore[x] = str(pkt)
                listNames[x] = playerName
                break
        if flag:
            listScore.append(str(pkt))
            listNames.append(playerName)
    else:
        for x in range(len(listNames)):
            if int(pkt) > int(listScore[x]):
                listScore.insert(x,str(pkt))
                listNames.insert(x, playerName)
                flag = False
                break
    
    f = open("TOP10Names.txt", mode="w+")
    for x in range(len(listNames)):
        f.writelines(f"{listNames[x]}\n")
    f.close()
    f = open("TOP10Score.txt", mode="w+")
    for x in range(len(listScore)):
        f.writelines(f"{listScore[x]}\n")
    f.close()
    
