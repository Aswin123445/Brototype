#this funtion delete an element from the array
#input data 
list=[0 for i in range(5)]
for i in range(5):
    list[i]=int(input())
#deleting the element of the specified position
pos=int(input("enter the position were you want to delete the element"))
list.pop(pos)
list.sort(reverse=True)
print(list)