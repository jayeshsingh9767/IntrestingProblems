arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    
print(arr)

