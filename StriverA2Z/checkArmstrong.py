import math

def countDigit(num):
    return int(math.log10(num)) + 1

def checkArmstrong(num):
    oldNum = num
    k = countDigit(num)
    ans = 0
    while num > 0:
        last = num % 10
        ans += last ** k
        num = num // 10
    if oldNum == ans:
        return True
    else:
        return False

print(checkArmstrong(371))
