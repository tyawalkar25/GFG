class Solution:
    def findFloor(self, arr,k):
        x = [i for i in arr if i <= k]
        if len(x) > 0:
            return arr.index(max(x))
        else:
            return -1


if __name__ == "__main__":
   ob = Solution()
   ans = ob.findFloor([2],1)
   print(ans)