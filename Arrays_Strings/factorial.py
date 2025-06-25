def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

n = 3
print(f"the factorial of {n} is {fact(n)}")