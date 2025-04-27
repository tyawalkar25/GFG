
from collections import Counter 
class Solution:
    def frequencyCount(self, arr):
        x = []
        n = len(arr)
        res = Counter(arr)
        for i in range(1,n+1):
            x.append(res[i])
        return x




if __name__ == "__main__":
   ob = Solution()
   ans = ob.frequencyCount([3, 3, 3, 3])
   print(ans)