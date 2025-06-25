def rev(a,first,last):
    while first < last:
        a[first],a[last] = a[last],a[first]
        first += 1
        last -= 1
    return a

a = [5,7,3,2,6,7,5,9]   
n = len(a)-1
print(rev(a,0,n))