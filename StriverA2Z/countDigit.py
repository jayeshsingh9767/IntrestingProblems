import math
def countDigit(num):
    return int(math.log10(num)) + 1

print(countDigit(3266))