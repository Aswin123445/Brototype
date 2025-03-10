def binary_search(li,left,right,value):
    if left > right:
        return None
    mid = int((left+right)/2)
    if li[mid] == value:
        return mid
    if value > li[mid]:
        return binary_search(li,mid+1,right,value)
    else :
        return binary_search(li,left,mid-1)

dat = [10,20,30,40] 
print(binary_search(dat,0,len(dat)-1,10))
        