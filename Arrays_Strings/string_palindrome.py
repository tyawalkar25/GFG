def is_palindrome(s,l,r):
    if l >= r:
        return True
    if (s[l] == s[r]):
        return is_palindrome(s,l+1,r-1)
    else:
        return False
   

s = 'dad'
n = len(s)-1
print(is_palindrome(s,0,n)) 
