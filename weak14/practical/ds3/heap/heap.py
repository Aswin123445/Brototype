#heapify max 
def max_heapify(arr,i,n):
    largest = i 
    left = i*2 + 1 
    right = i*2 + 2 
    if left < n and arr[left] > arr[largest] :
        largest = left 
    if right < n and arr[right] > arr[largest] :
        largest = right 
    if largest != i :
        arr[largest],arr[i] = arr[i],arr[largest]
        max_heapify(arr,largest,n)
        
#finding the right chile we can use the formula i*2 + 2 
def right_child(arr,i):
        right_child = i*2 + 2 
        if right_child < len(arr):
            return arr[right_child]
        else :
            return 'there is no right child for this particular element'

def heap_sort(arr):
    n = len(arr)
    #convert it inot a heap sort 
    for i in range(n//2-1,-1,-1):
        max_heapify(arr,i,n)
        
    #swapping element on heap 
    for i in range(len(arr)-1,-1,-1):
        #swap
        arr[i],arr[0] = arr[0],arr[i]
        #destructure 
        max_heapify(arr,0,i)
a = [10,20,22,12,44]
heap_sort(a)
print(a)
print(right_child(a,1))

#Implement Min-Heap
class Heap:
    def __init__(self):
        self.heap = []
    def get_parent(self,index):
        return (index-1)//2
    def get_left_child(self,index):
        return 2*index + 1 
    def get_right_child(self,index):
        return 2*index + 2 
    def push(self,data):
        self.heap.append(data)
        self.up_heapify(len(self.heap) - 1 )
    def up_heapify(self,index):
        while index > 0 and self.heap[index] < self.heap[self.get_parent(index)]:
            self.heap[index],self.heap[self.get_parent(index)] = self.heap[self.get_parent(index)],self.heap[index]
            #moving up 
            index = self.get_parent(index)
    def pop(self):
       if not self.heap :
            return None 
       if len(self.heap) == 1 :
           return self.heap.pop()
       minimum = self.heap[0]
       self.heap[0] = self.heap.pop()
       self.down_heapify(0)
       return minimum
    def down_heapify(self,index):
       lowest = index 
       n = len(self.heap)
       left = self.get_left_child(index)
       right = self.get_right_child(index)
       if left < n and self.heap[left] < self.heap[lowest]:
           lowest = left
       if right < n and self.heap[right] < self.heap[lowest]:
           lowest = right
       if lowest != index :
           self.heap[lowest],self.heap[index] = self.heap[index],self.heap[lowest]
           self.down_heapify(lowest)
           
    def display(self):
        print(self.heap)
        
s = Heap()
s.push(10)
s.push(1)
s.push(33)
s.push(400)
s.push(34)
s.display()
s.pop()
s.display()     