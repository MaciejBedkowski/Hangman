def GetPasswords(list):
    f = open("password.txt")
    for line in f.readlines():
        list.append(line.strip())
    f.close()
    return list
