# Two pointer approach
# Given an array of integers and a target sum, the task is to check if there are two numbers in the array that add up to the target sum.
# Time Complexity - O(nlogn)
# Space Complexity - O(1)
class Solution:
    def twoSum(self, arr,target):
        arr.sort()
        if len(arr) < 2:
            return False
        else:
            low,high = 0,len(arr)-1
            while low < high:
                if arr[low] + arr[high] > target:
                    high = high-1
                elif arr[low] + arr[high] < target:
                    low = low+1
                else:
                    return True

        return False



 
if __name__ == "__main__":
   ob = Solution()
   ans = ob.twoSum([1,2,3,4],7)
   print(ans)