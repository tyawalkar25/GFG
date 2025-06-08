def reverse_number(n):
    num = n
    rev = num%10
    while(num//10 > 0):
        num = num//10
        last = num%10
        rev = last + rev*10
    if n == rev:
        return "Palindrome"
    else:
        return "Not a palindrome"
    
n = 567765
print(f"The number {n} is {reverse_number(n)}")