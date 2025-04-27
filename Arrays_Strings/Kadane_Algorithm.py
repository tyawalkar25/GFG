class Solution:
    def maxSubArraySum(self, arr):
        res = arr[0]
        maxending = arr[0]
        for i in range(1,len(arr)):
            maxending = max(maxending+arr[i],arr[i])
            res = max(res,maxending)
        return res


if __name__ == "__main__":
   ob = Solution()
   ans = ob.maxSubArraySum([2, 3, -8, 7, -1, 2, 3])
   print(ans)