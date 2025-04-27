class Solution:
    def firstRepeated(self, arr):
        d = {}
        ans = 9999999999999999
        for i,e in enumerate(arr):
           if e in d:
               if d[e] < ans and ans != -1:
                  ans = d[e]
           else:
               d[e] = i
        if ans < 9999999999999999:
            return ans+1
        else:
            return -1 



 
if __name__ == "__main__":
   ob = Solution()
   ans = ob.firstRepeated([1, 5, 1, 4, 3, 5, 6])
   print(ans)