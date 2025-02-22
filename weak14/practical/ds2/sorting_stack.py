class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.is_empty():
            return print('stack is empty')
        return self.stack.pop()
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
    def display(self):
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i],end=" ")
    def sort(self):
        if self.is_empty():
            print('stock is empty')
            return 
        temp_stock = Stack()
        while not self.is_empty():
            temp = self.pop()
            while not temp_stock.is_empty() and temp < temp_stock.peak():
                self.push(temp_stock.pop())
            temp_stock.push(temp)
        while not temp_stock.is_empty():
            self.push(temp_stock.pop())
            
s = Stack()
s.push(10)
s.push(2000)
s.push(100)
s.sort()
s.display()