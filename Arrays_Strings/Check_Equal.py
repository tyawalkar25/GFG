from collections import Counter
class Solution:
    def checkEqual(self, a,b):
        dir_a = Counter(a)
        dir_b = Counter(b)
        return dir_a == dir_b


if __name__ == "__main__":
   ob = Solution()
   ans = ob.checkEqual([1, 2, 5],[2, 4, 15])
   print(ans)


 