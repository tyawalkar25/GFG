def get_factorial(n):
    fact = [1]
    div_count = int(n/2)
    for i in range(2,div_count+1):
        if n/i - n//i == 0:
            fact.append(n//i)
    fact.sort()
    fact.append(n)
    return fact
    
n = 17
print(f"The factorial of {n} is {get_factorial(n)}")



# 30 - [1,2,3,5,6,10,15,30]