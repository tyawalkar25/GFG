def count_digits(n):
    last = n%10
    count = 0
    while (n > 0):
        print(last)
        count += 1
        n = n // 10
        last = n % 10
    return count
    

print(f"Total number of digits in the integer : {count_digits(5873)}" )
    
