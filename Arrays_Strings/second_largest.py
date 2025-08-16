class Solution:
    def getSecondLargest(self, arr):
        max = arr[0]
        n = len(arr)
        for i in range(1,len(arr)):
            if arr[i] > max:
                max = arr[i]
        diff = max - arr[0]
        for i in range(1,n):
            if arr[i] != max:
                diff = min(diff, (max - arr[i]))
        x = max - diff
        return x
            


if __name__ == "__main__":
   ob = Solution()
   ans = ob.getSecondLargest([33,12,55,-4,0,10,99])
   print(ans)
        