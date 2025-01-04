def printNum(i):

    if i < 1:
        return
    print(i)
    printNum(i-1)

printNum(10)