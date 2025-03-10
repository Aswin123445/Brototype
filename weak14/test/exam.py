class Node :
    def __init__(self,data):
        self.data =  data
        self.next = None 
class Stack :
    def __init__(self):
        self.stack = None
    def is_empty(self):
        return self.stack == None 
    def push(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.stack = new_node
            return 
        new_node.next = self.stack
        self.stack = new_node
    def pop(self):
        if self.is_empty():
            print('stack is already empty')
            return 
        self.stack = self.stack.next 
    def display(self):
        if self.is_empty():
            print('stack is  empty')
            return 
        temp = self.stack
        while temp :
            print(temp.data,end='->')
            temp = temp.next
        print()       
s = Stack()
s.push(10)
s.push(20)
s.display()
s.pop()
s.display()

a = [64, 34, 25, 12, 22, 11, 90]
def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
insertion_sort(a)
print(a)