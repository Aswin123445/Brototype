def quick_sort(arr,lb,ub):
    if lb < ub :
        pivot_pos = partion(arr,lb,ub)
        quick_sort(arr,lb,pivot_pos-1)
        quick_sort(arr,pivot_pos+1,ub)
def partion(arr,lb,ub):
    start = lb
    end = ub
    pivot = arr[lb]
    while start < end :
        while start < ub and arr[start] <= pivot :
            start +=1
        while end > lb and arr[end] > pivot :
            end -= 1
        if start < end :
            arr[start],arr[end] = arr[end],arr[start]
    arr[lb],arr[end] = arr[end],arr[lb]
    return end

asw= [1,2,34,45,532,2]
    
quick_sort(asw,0,len(asw)-1)
print(asw)
