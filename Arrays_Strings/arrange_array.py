class Solution:
    def arrangearray(self, nums):
        n = len(nums)
        if n == 1:
            return nums
        i = 0
        for j in range(1,n):
            if nums[j] != nums[i]:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]

        return nums,i+1
            


if __name__ == "__main__":
   ob = Solution()
   arranged_array,unique_count = ob.arrangearray([1,1,1,2,3,4,4,7,9,9,9,10])
   print(f"the arranged array is : {arranged_array}")
   print(f"Count of unique elements in the given array is : {unique_count}")

# [1, 2, 3, 4, 7, 9, 10, 0, 0, 0, 0, 0]