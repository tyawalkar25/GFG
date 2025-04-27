class Solution:
    def findPair(self, arr,x):
        arr.sort()
        n = len(arr)
        low,high = 0, 1
        while low < n and high < n:
            if low != high and (arr[high] - arr[low]) == x:
                return 'true'
            elif (arr[high] - arr[low]) < x:
                high = high + 1
            else:
                low = low + 1
                
            

        return 'false'
        

if __name__ == "__main__":
   ob = Solution()
   ans = ob.findPair([2,5,3,4,3,3,2],8)
   print(ans)

  