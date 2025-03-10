class Stack:
    def __init__(self):
        self.array = []
    def push(self,data):
        self.array.append(data)
    def pop(self):
       return self.array.pop()
    def display(self):
        print(self.array)
   
class Queue:
    def __init__(self):
        self.size = 5
        self.array = [None]*self.size
        self.front = -1
        self.rear = -1 
    def is_empty(self):
        return self.front == -1
    def is_full(self):
        return self.rear == self.size-1
    def enqueu(self,data):
        if self.is_full():
            print('queue is full')
            return 
        if self.is_empty():
            self.front += 1
        self.rear += 1
        self.array[self.rear]=data
    def dequeu(self):
        if self.is_empty():
            print('queue is already empty')
            return 
        remover = self.array[self.front]
        if self.rear == self.front:
            self.rear = self.front = -1
        self.front += 1
        return remover
    def display(self):
        if self.is_empty():
            print('queue is already empty')
            return 
        print(self.array[self.front:self.rear+1])
        
    #reverseing 
q = Queue()
q.enqueu(100)
q.enqueu(140)
q.enqueu(300)
q.enqueu(503)
q.display()
#pushing to the stack
s = Stack()
s.push(q.dequeu())
s.push(q.dequeu())
s.push(q.dequeu())
s.push(q.dequeu())
#reversing the queue

q.enqueu(s.pop())
q.enqueu(s.pop())
q.enqueu(s.pop())
q.enqueu(s.pop())
q.display()