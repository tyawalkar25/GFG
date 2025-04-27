class Solution:
    def pushZerosToEnd(self, arr):
        count = 0
        n = len(arr)
        for i in range(n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        while count < n:
            arr[count] = 0
            count += 1

        return arr

        

if __name__ == "__main__":
   ob = Solution()
   ans = ob.pushZerosToEnd([1, 2, 3])
   print(ans)