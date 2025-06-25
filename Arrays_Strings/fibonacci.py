def fibn(n):
    if n == 0 or n == 1:
        return n
    return fibn(n-1) + fibn(n-2)

n = 5
print(fibn(n))