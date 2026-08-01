class Solution:
    def rearrange(self, arr):
        result = [0] * len(arr)
        pos, neg = 0,1
        for i in arr:
            if i > 0:
                result[pos] = i
                pos = pos + 2
            else:
                result[neg] = i
                neg = neg + 2
        return result

if __name__ == "__main__":
   ob = Solution()
   ans = ob.rearrange([5,10,-3,-2,-6,25])
   print(ans)

#[9, -2, 4, -1, 5, -5, 0, -3, 2]