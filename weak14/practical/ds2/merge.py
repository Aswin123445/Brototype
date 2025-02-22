def merge_sort(arr,lb,ub):
    if lb < ub :
        mid = int((lb+ub)/2)
        merge_sort(arr,lb,mid)
        merge_sort(arr,mid+1,ub)
        merge(arr,lb,mid,ub)
def merge(arr,lb,mid,ub):
    i = lb
    j = mid + 1
    temp = []
    while i <= mid and j <= ub :
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i+=1
        else :
            temp.append(arr[j])
            j += 1
    if i > mid :
        while j <= ub :
            temp.append(arr[j])
            j += 1
    else :
       while i <= mid :
            temp.append(arr[i])
            i += 1
    for s in range(len(temp)):
        arr[lb + s] = temp[s]
asw = [20,1,44,44,35,345]
merge_sort(asw,0,len(asw)-1)
print(asw)