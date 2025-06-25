def rev(a,first,last):
    if first >= last:
        return a
    a[first],a[last] = a[last],a[first]
    
    return rev(a,first+1,last-1)

a = [5,7,3,2,6,7,5,9]   
n = len(a)
print(rev(a,2,5))