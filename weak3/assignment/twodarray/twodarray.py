#comprehensive list
list=[[0]*3 for i in range(3)]
list1=[[0]*3 for i in range(3)]
sum=[[0]*3 for i in range(3)]
#assigning values to the array
print("enter values")
for i in range(3):
    for j in range(3):
        list[i][j]=int(input())
print("enter values of second list")
for i in range(3):
    for j in range(3):
        list1[i][j]=int(input())
#finding the sum of the list
for i in range(3):
    for j in range(3):
        sum[i][j]=list[i][j]+list1[i][j]
print(sum)
