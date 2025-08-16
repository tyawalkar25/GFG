def find_missing_number(arr):
    n = len(arr)
    total_sum = int((n * (n+1))/2)
    array_sum = 0
    for i in arr:
        array_sum += i
    return total_sum - array_sum
    

print(find_missing_number([0,1,2,4,5]))