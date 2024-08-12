#removing 2 elements next after ocurance of prime number in the list
size=int(input("enter the size of the list"))
list=[0 for i in range(size)]
#funtion to find the prime number 
def is_prime(data):
    if(data<2):
        return False
    count=2
    while(count<data):
        if(data%count==0):
            return False
        count+=1
    return True
#inputing elements to the list
for i in range(len(list)):
    list[i]=int(input())
#iterating through the list
i=0
while(i<len(list)):
    if(is_prime(list[i])):
        list.pop(i)
    i+=1
print(list)
