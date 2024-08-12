list=[0 for i in range(6)]
print("enter elements to the list")
for i in range(6):
    list[i]=int(input())
#making separate array for  odd and even 
list2=[x for x in list if x%2==0]
list3=[x for x in list if x%2!=0]
print("{}\n{}".format(list2,list3))