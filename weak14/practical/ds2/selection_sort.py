def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min is not i :
            arr[min],arr[i] = arr[i],arr[min]
    print(arr)
selection_sort([20,1,33,33,2,44,34,5])