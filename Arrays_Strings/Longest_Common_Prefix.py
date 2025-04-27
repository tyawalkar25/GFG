class Solution:
    def checkEqual(self, a):
        c_prefix = a[0]
        for s in a[1:]:
            while not s.startswith(c_prefix):
                c_prefix = c_prefix[:-1]

                if not c_prefix:
                    return ""

        return c_prefix

        
        


if __name__ == "__main__":
   ob = Solution()
   ans = ob.checkEqual(["ab","a","a"])
   print(ans)