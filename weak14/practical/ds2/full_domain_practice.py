#fibonocci 
def fibonocci(n):
    if n < 2 :
        return n 
    
    s1 = fibonocci(n-1)
    s2 = fibonocci(n-2)
    return s1 + s2
    
print([fibonocci(i) for i in range(10)])

#reverse string using recursion 
def reverse(s):
    if not s :
        return ""
    data = reverse(s[1:])
    return data + s[0]

print(reverse('sandeep'))

def sumarray(l):
    if not l :
        return 0 
    value = sumarray(l[1:])
    return value + l[0]

d = [10,2,3,45,43,565,3]