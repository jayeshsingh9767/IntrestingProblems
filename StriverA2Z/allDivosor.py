def getAllDiisor(num):
    ans = []
    for i in range(1, num):
        if (num % i) == 0:
            ans.append(i)
    return ans

print(getAllDiisor(36))