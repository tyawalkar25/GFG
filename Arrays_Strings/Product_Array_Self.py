class Solution:
    def productExceptSelf(self, arr):
        zeros = 0
        idx = -1
        prod = 1
        for i in range(len(arr)):
            if arr[i] == 0:
                zeros += 1
                idx = i
            else:
                prod = prod * arr[i]
        res = [0] * len(arr)
        if zeros == 0:
            for i in range(len(arr)):
                res[i] = prod // arr[i]
        elif zeros == 1:
            res[idx] = prod
        return res




 
if __name__ == "__main__":
   ob = Solution()
   ans = ob.productExceptSelf([10,3,5,6,2])
   print(ans)