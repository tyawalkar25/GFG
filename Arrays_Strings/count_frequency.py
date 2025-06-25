nums = [1,2,3,3,4,5,1,6,6,6,2,2,2,2,2,2]

count_dict = {}

for i in nums:
    count_dict[i] = count_dict.get(i,0) + 1

print(count_dict)