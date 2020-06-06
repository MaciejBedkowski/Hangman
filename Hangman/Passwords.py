def GetPasswords(list, choiceCategory):
    if choiceCategory == 1:
        f = open("heroePassword.txt")
        for line in f.readlines():
            list.append(line.strip())
        f.close()
        return list
    elif choiceCategory == 2:
        f = open("filmsPassword.txt")
        for line in f.readlines():
            list.append(line.strip())
        f.close()
        return list
    elif choiceCategory == 3:
        f = open("animalsPassword.txt")
        for line in f.readlines():
            list.append(line.strip())
        f.close()
        return list

