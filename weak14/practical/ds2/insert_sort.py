def insert_sort(arr):
    for i in range(1,len(arr)):
        j = i - 1 
        temp = arr[i]
        while j >= 0 and arr[j] > temp :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    print(arr)
insert_sort([1,1000,34,532,88,33,455,34,566])