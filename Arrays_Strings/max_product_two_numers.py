# Given an integer array arr, find two numbers such that their product is maximum and return the maximum product.
# Time Complexity: O(n) 
# Space Complexity: O(1)
class Solution:
    def maxProduct(self,arr):
        max1,max2,min1,min2 = arr[0],float("-inf"),arr[0],float("inf")
        for i in range(1,len(arr)):
            if arr[i] > max1:
                max2 = max1
                max1 = arr[i]
            elif arr[i] > max2:
                max2 = arr[i]
            if arr[i] < min1:
                min2 = min1
                min1 = arr[i]
            elif arr[i] < min2:
                min2 = arr[i]
        return max(max1*max2,min1*min2)


if __name__ == "__main__":
    ob = Solution()
    ans = ob.maxProduct([-10,5,4,-2,0,-3])
    print(ans)