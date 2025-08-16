# time complexity - O(n*n) worst case
# space complexity - O(1)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr



arr = [1,5,3,7,9,6,2,8]
print(insertion_sort(arr))