#heap sorting 
def heapify_max(arr,i,n):
    largest = i 
    left = 2*i + 1 
    right = 2*i + 2 
    if left < n and arr[left] > arr[largest] :
        largest = left
    if right < n and arr[right] > arr[largest] :
        largest = right 
    if largest != i :
        arr[largest],arr[i] = arr[i],arr[largest] 
        heapify_max(arr,largest,n)
        
def heapify_min(arr,i,n):
    smallest = i 
    left = 2*i + 1 
    right = 2*i + 2 
    if left < n and arr[left] < arr[smallest] :
        smallest = left
    if right < n and arr[right] < arr[smallest] :
        smallest = right 
    if smallest != i :
        arr[smallest],arr[i] = arr[i],arr[smallest] 
        heapify_max(arr,smallest,n)
        
#implenting heap sort 

def heap_sort(arr):
    n = len(arr)
    #convert list to heap :
    for i in range(n//2 -1 ,-1,-1):
        heapify_min(arr,i,n)
    print(arr)
        
    #compare and swap :
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify_min(arr,0,i)
        
a = [10,30,4,23,45]

heap_sort(a)
print(a)
         
        
