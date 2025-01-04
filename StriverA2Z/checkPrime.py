def checkPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

import math
def checkPrime2(num):
    count = 0
    for i in range(1, int(math.sqrt(num))+1):
        if (num % i) == 0:
            count += 1
            if (num // i) != i:
                count += 1
    if count == 2:
        return True
    return False  

print(checkPrime2(21)) 

