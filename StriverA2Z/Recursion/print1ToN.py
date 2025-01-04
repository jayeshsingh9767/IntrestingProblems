i = 0
num = 20
def prinNum():
    global i, num
    if (i > num):
        return
    print(i)
    i += 1
    prinNum()

prinNum()