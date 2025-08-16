class Solution:
    def returnsortedornot(self, arr):
        n = len(arr)
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                return False
        return True
            


if __name__ == "__main__":
   ob = Solution()
   ans = ob.returnsortedornot([1,1,1,3,5])
   print(ans)