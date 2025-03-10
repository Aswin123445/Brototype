class MinHeap:
    def __init__(self):
        self.heap = []
    def push(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    def heapify_up(self,index):
        parent = (index-1)//2 
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
            index = parent 
            parent = (index - 1)//2
            
    def pop(self):
        if self.heap is None :
            return None 
        if len(self.heap) == 1 :
            self.heap.pop()
            return 
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_value
    
    def heapify_down(self,index):
        n = len(self.heap)
        small = index
        left = index*2 + 1 
        right = index*2 + 2
        if left < n and self.heap[left] < self.heap[small]:
            small = left
        if right < n and self.heap[right] < self.heap[small]:
            small = right
        if small != index :
            self.heap[index],self.heap[small] = self.heap[small],self.heap[index]
            self.heapify_down(small)
    def display(self):
        print(self.heap)
        
    
p = MinHeap()
p.push(10)
p.push(30)
p.push(5)
p.push(100)
p.push(44)
p.push(88)
p.pop()
p.display()

        