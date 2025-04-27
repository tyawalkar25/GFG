
class Solution:
    def peakElement(self, arr):
        x = max(arr)
        return arr.index(x)




if __name__ == "__main__":
   ob = Solution()
   ans = ob.peakElement([1, 2, 4, 5, 7, 8, 3])
   print(ans)