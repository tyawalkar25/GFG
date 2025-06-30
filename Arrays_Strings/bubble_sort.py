# time complexity - O(n*n) worst case, best case O(n)
# space complexity - O(1)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr



arr = [1,5,3,7,9,6,2,8]
print(bubble_sort(arr))