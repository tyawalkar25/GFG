class Solution:
    def longestUniqueSubstr(self, s):
        res = s[0]
        long_str = s[0]
        for i in s[1:]:
            if i not in long_str:
                long_str = long_str + i
                if len(long_str) >= len(res):
                    res = long_str
            else:
                long_str = i
        return len(res)




if __name__ == "__main__":
   ob = Solution()
   ans = ob.longestUniqueSubstr("abcdefabcbb")
   print(ans)