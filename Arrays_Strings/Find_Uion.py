class Solution:
    def findUnion(self, a,b):
        return len(set(a).union(set(b)))


if __name__ == "__main__":
   ob = Solution()
   ans = ob.findUnion([1, 2, 1, 1, 2],[2, 2, 1, 2, 1])
   print(ans)