list=[]
size=int(input("enter the size of the list"))
print("enter the elements to the list")
for i in range(size):
    data=int(input("enter values"))
    list.append(data)
#doing selection sort logic
for i in range(size-1):
    #selection sort select the lowest element from the unseroted list and
    #place it in the sorted list
    min=i
    for j in range(i+1,size):
        if(list[min]>list[j]):
            #the unsorted list as the lowest element
            min=j
    if min!=i:
        #swapping elements
        list[i],list[min]=list[min],list[i]
print(list)