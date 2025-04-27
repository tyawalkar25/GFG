class Solution:
    def isPalindrome(self,s):
        rev =  s[::-1]
        if (s == rev):
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    ans = s.isPalindrome('acbca')
    
    print(ans)