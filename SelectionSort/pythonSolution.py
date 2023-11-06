def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        # find minimum value in rest of array
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


a = [2,4,1,5,3]
print(selection_sort(a))