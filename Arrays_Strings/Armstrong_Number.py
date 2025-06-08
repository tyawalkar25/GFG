def is_armstrong(n):
    len = 1
    num = n
    a = [num%10]
    res = 0
    while(num//10 > 0):
        num = num//10
        len += 1
        a.append(num%10)
    for i in a:
        res = res + i**len
    if n == res:
        return "Is Armstrong number"
    else:
        return "Not an arnstrong number"
        



n = 123
print(f"The number {n} is {is_armstrong(n)}")