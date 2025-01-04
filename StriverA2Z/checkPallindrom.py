def checkPallindrom(num):
    temp = num
    rev = 0
    while temp > 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    if rev == num:
        return True
    else:
        return False
    
print(checkPallindrom(878))