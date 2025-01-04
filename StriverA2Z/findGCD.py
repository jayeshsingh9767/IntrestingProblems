def getGcd(num1, num2):
    minNum = min(num1, num2)
    for i in range(minNum, 1, -1):
        if (num1 % i == 0) and (num2 % i == 0):
            return i
    else:
        return 1
    
print(getGcd(16, 24))
