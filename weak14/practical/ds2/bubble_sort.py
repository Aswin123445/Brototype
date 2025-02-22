class BubbleSort:
    def __init__(self,arr):
        self.arr = arr
    def bubble_sort(self):
        sort_list = self.arr
        for i in range(len(sort_list)-1):
            is_swapped = False
            for index in range(len(sort_list)-1-i):
                if sort_list[index] > sort_list[index + 1]:
                    sort_list[index],sort_list[index + 1] = sort_list[index+1],sort_list[index]
                    is_swapped = True
            if is_swapped == False :
                break
        print(sort_list)
    def insert_sort(self):
        temp = self.arr
        for i in range(1,len(temp)):
            key = temp[i]
            sort = i-1
            while sort>= 0 and temp[sort]>key:
                temp[sort+1] = temp[sort]
                sort -= 1
            temp[sort+1]  = key
        print(temp)
        
    def selection_sort(self):
        array = self.arr
        for i in range(len(array)-1):
            min = i
            for j in range(i+1,len(array)):
                if array[j]<array[min]:
                    min = j
            array[i],array[min] = array[min],array[i]
        print(array)

def partition(arr,lb,ub):
    pivot = arr[lb]
    start = lb 
    end = ub
    while start < end :
        while start <= ub and arr[start] <= pivot :
            start += 1 
        while end > lb and arr[end] > pivot :
            end -= 1
        if start < end :
            arr[start],arr[end] = arr[end],arr[start]
    arr[lb],arr[end] = arr[end] ,arr[lb]
    return end
def quick_sort(arr ,lb , ub ):
    if lb < ub :
        loc =  partition(arr,lb,ub)
        quick_sort(arr,lb,loc-1)
        quick_sort(arr,loc+1,ub)
        
def merge_sort(arr,lb,ub):
    if lb < ub :
        mid = int((lb + ub)/2)
        merge_sort(arr,lb,mid)
        merge_sort(arr,mid+1,ub)
        merge(arr,lb,mid,ub)
def merge(arr,lb,mid,ub):
    i = lb
    j = mid + 1
    array = []
    while i <= mid and j <= ub:
        if arr[i] <= arr[j]:
            array.append(arr[i])
            i += 1 
        else :
            array.append(arr[j])
            j += 1 
    if i > mid :
        while j <= ub :
            array.append(arr[j])
            j+=1
    else :
        while i <= mid:
            array.append(arr[i])
            i += 1 
    for k in range(len(array)):
        arr[lb + k] = array[k]
# sort = BubbleSort([10,43,33,44,55,334,1])
# sort.selection_sort()
aswin =  [ 10,3,100,32,43,54,2000 ]
# quick_sort(aswin,0,len(aswin)-1)
# print(aswin)
merge_sort(aswin,0,len(aswin)-1)
print(aswin)


