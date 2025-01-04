def callMe(i, num):
    if i > num:
        return
    print("I am Jayesh")
    callMe(i+1, num)

callMe(0, 10)
