def max_sum_subarray(arr):
    n = len(arr)
    max_sum = arr[0]
    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum = curr_sum + arr[j]
            max_sum = max(max_sum,curr_sum)
            

    return max_sum  
    

print(max_sum_subarray([1,2,3,0,4]))