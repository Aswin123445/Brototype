#binary recursion
class Binary:
    def __init__(self,list):
        self.list = list 
    def binary_search(self,arr,left,right,value):
        if left>right:
            return None
        mid = int((left + right )/2)
        if arr[mid] == value :
            return mid + 1
        if arr[mid] > value :
            return self.binary_search(arr,left ,mid-1,value)
        return self.binary_search(arr,mid+1,right,value)
    #third largest element in a array
    def third_largest(self):
        first = second = thrid = 0
        if len(self.list) < 3 :
            return None
        for i in self.list:
            #largest element 
            if i > first :
                thrid = second
                second = first
                first = i
            elif i > second :
                third = second
                second = i
            elif i > third :
                third = i
        print (f'{first} {second} {thrid}')
        return thrid
            
    
data = Binary([10,20,30,40,50])
data2 = Binary([50,20,0,25,100])
pos = data.binary_search(data.list,0,len(data.list)-1,30)
print(pos)

def adding_sum(num):
    if num == 0:
        return num
    value = adding_sum(num-1)
    return value + num

print(adding_sum(4))
print(data2.third_largest())


    