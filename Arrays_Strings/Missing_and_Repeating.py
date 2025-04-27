class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        gaussian_sum = int((n * (n + 1)) / 2)
        arr_sum = sum(arr)
        set_sum = sum(set(arr))

        duplicate = arr_sum - set_sum
        
        missing = gaussian_sum - set_sum

        return [duplicate, missing]




if __name__ == "__main__":
   ob = Solution()
   ans = ob.findTwoElement([1,1,2])
   print(ans)