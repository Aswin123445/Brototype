def reverse(stirng):
    end = len(stirng)-1 
    start = 0
    li = [None]*len(stirng)
    while start <= end :
        li[start] = stirng[end]
        li[end] = stirng[start]
        start += 1 
        end -= 1
    print(''.join(li))
    #print(''.join(li))
    return stirng[::-1]

print(reverse('aswin'))