# Time complexity - O(nlogn)
# Space complexity - O(n)
def merge_array(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    i,j = 0,0
    result = []
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    if i < n:
        while i < n:
            result.append(arr1[i])
            i += 1
    if j < m:
        while j < m:
            result.append(arr2[j])
            j += 1
    return result


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    left_nums = merge_sort(left)
    right_nums = merge_sort(right)
    return merge_array(left_nums,right_nums)
    

print(merge_sort([1,5,3,7,9,6,2,8,4]))