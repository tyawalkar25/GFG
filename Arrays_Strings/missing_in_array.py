def missing_array(arr):
    xor,i=0,0
    while i<len(arr):
        xor^=(i+1)^arr[i]
        i+=1
    return xor^(i+1)

print(missing_array([9]))




