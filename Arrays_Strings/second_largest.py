class Solution:
    def getSecondLargest(self, arr):
        s = sorted(set(arr))
        if (len(s) == 1):
            return -1
        else:
            if(s[-2] > s[-1]):
                return -1
            else:
                return s[-2]



if __name__ == "__main__":
   ob = Solution()
   ans = ob.getSecondLargest([10])
   print(ans)
        