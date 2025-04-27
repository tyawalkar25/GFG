class Solution:
    def areAnagrams(self, s1,s2):
        return ''.join(sorted(s2))


if __name__ == "__main__":
   ob = Solution()
   ans = ob.areAnagrams("allergy","allergic")
   print(ans)