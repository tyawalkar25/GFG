def max_consecutive_one(arr):
    n = len(arr)
    curr_count, max_count = 0,0
    for i in range(n):
        if arr[i] == 1:
            curr_count += 1
            max_count = max(curr_count, max_count)
        else:
            curr_count = 0

        
    return max_count
    

print(max_consecutive_one([1,0,1,0,1,1,1]))