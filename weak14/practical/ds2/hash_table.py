# class HashTable:
#     def __init__(self):
#         self.size = 10
#         self.array = [[] for _ in range(self.size)]
#     def get_hash(self,key):
#         return hash(key)%self.size
#     def insert(self,key,value):
#         index = self.get_hash(key)
#         found = False
#         for i in self.array[index]:
#             if i[0] == key :
#                 i[1] == value
#                 found = True
#         if not found :
#             self.array[index].append([key,value])
#     def get(self,key):
#         index = self.get_hash(key)
#         for value in self.array[index]:
#             if value[0] == key :
#                 print(value[1])
#                 return 
#     def display(self):
#         for i , data in enumerate(self.array):
#             print(f'index {i} and data is {data}')
#     def delete(self,key):
#         index = self.get_hash(key)
#         for i ,data in enumerate(self.array[index]):
#             if data[0] == key :
#                 del self.array[index][i]
#         return False
    
# s = HashTable()
# s.insert('aswin',20)
# s.insert('manoj',50)
# s.insert('biju',20)
# s.display()
# s.get('biju')
# s.delete('biju')
# s.display()

# #hashtable for two sum
# def twosum(arr,target):
#     ha = {}
#     for i,data in enumerate(arr):
#         complentment = target-data
#         if complentment in ha :
#             return [i,ha[complentment]]
#         else :
#             ha[data] = i
            
# def occurance(string):
#     di = {}
#     for char in string:
#         if char in di :
#             di[char] += 1
#         else :
#             di[char] = 1
#     return di
# print(occurance('aswinn'))
# #non-repeating charater
# def non_repeating_character(string):
#     di = {}
#     for char in string:
#         di[char] = di.get(char,0) + 1
#     for chr in string :
#         if di[chr] == 1:
#             return chr
# print(non_repeating_character('missippi'))


class HashTable:
    def __init__(self):
        self.size = 10
        self.array = [[] for _ in range(self.size)]
    def get_hash(self,key):
        return hash(key)%self.size
    def insert(self,key,data):
        index = self.get_hash(key)
        for _ in self.array[index]:
            if _[0] == key :
                _[1] = data
        self.array[index].append([key,data])
    def get(self,key):
        index = self.get_hash(key)
        for _ in self.array[index]:
            if _[0] == key:
                print(_[1])
            
    def delete(self,key):
        index = self.get_hash(key)
        for i,data in enumerate(self.array[index]):
            if data[0] == key:
                del self.array[index][i]
            
    def display(self):
        for i,data in enumerate(self.array):
            print(f'index = {i} and data = {data}')
            
s = HashTable()
s.insert('aswin',20)
s.display()
s.delete('asswin')
s.display()
s.delete('aswin')
s.display()
#quick sort 
def quick_sort(arr,lb,ub):
    if lb < ub :
        loc = partition(arr,lb,ub)
        quick_sort(arr,lb,loc-1)
        quick_sort(arr,loc+1,ub)
        
def partition(arr,lb,ub):
    start = lb 
    end = ub 
    pivot = arr[lb]
    while start < end :
        while arr[start] <= pivot :
            start += 1
        while arr[end]  > pivot :
            end -= 1 
        if start < end :
            arr[start],arr[end] = arr[end],arr[start]
    arr[lb],arr[end] = arr[end],arr[lb]
    return end
    
a = [10,3,33,44,32]
quick_sort(a,0,len(a)-1)
print(a)


def merge_sort(a,lb,ub):
    if lb < ub :
        mid = (lb + ub)//2
        merge_sort(a,lb,mid)
        merge_sort(a,mid+1,ub)
        merge(a,lb,mid,ub)
        
def merge(a,lb,mid,ub):
    i = lb 
    j = mid + 1 
    temp_arr = []
    while i <= mid and j <= ub :
        if a[i] <= a[j] :
            temp_arr.append(a[i])
            i += 1 
        else :
            temp_arr.append(a[j])
            j += 1 
    if i > mid :
        while j <= ub :
            temp_arr.append(a[j])
            j += 1 
    else :
        while i <= mid :
            temp_arr.append(a[i])
            i += 1 
    for k in range(len(temp_arr)):
        a[lb + k] = temp_arr[k]
        
b = [100,200,1,40,50]
merge_sort(b,0,len(b)-1)
print(b)
            
    
        
            
