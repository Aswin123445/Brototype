#insertion sort
#one item is selected from the unserted sublist and put in the appropirate place
list=[]
#taking the data
size=int(input("enter the size of the data"))
for i in range(size):
    data=int(input("enter value"))
    list.append(data)
#putting insertion logic
for i in range(1,size-1):
    temp=list[i]
    j=i-1
    while j>=0 and list[j]<temp:
        list[j+1]=list[j]
        j-=1
    list[j+1]=temp
print(list)