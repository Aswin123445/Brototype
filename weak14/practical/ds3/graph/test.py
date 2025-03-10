class Heap:
    def __init__(self):
        self.heap = []
    def pop(self):
        if not self.heap :
            return 
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
            self.heap[small],self.heap[index] = self.heap[index],self.heap[small]
            self.heapify_down(small)
            
    def display(self):
        print(self.heap)
            

h = Heap()
h.heap = [10,15,20] 
h.pop()
h.display()