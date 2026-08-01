def two_sum(arr,target):
    n = len(arr)
    dict = {}
    for i in range(n):
        diff = target - arr[i]
        if diff in dict:
            return [dict[diff],i]
        dict[arr[i]] = i
        
    

print(two_sum([9,3,2,100,6,12,1,-3,-4,-1,20],6))