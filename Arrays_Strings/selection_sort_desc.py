def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max = i
        for j in range(i+1,n):
            if arr[j] > arr[max]:
                max = j
        arr[i],arr[max] = arr[max],arr[i]
    return arr


print(selection_sort([1,4,2,8,9,6,14]))