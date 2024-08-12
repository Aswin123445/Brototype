list=[0 for i in range(10)]
listp=[]
#funtion to find the prime number
def is_prime(num):
    if(num<=1):
        return False
    count=2
    while(count<num):
        if(num%count==0):
            return False
        count+=1
    return True
print("enter elements you to to input")
for i in range(10):
    list[i]=int(input())
#checking for prime number
for i in range(10):
    if(is_prime(list[i])):
        listp.append(list[i])
#finding the average
sum=0
for i in range(len(listp)):
     sum+=listp[i]
print("average of sum is {}".format(sum/len(listp)))

