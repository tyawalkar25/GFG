class Solution:
    def checkEqual(self, arr):
        n = len(arr)
        res = []
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if (arr[i] + arr[j] + arr[k] == 0):
                        res.append([i,j,k])
        return res



if __name__ == "__main__":
   ob = Solution()
   ans = ob.checkEqual([0, -1, 2, -3, 1])
   print(ans)