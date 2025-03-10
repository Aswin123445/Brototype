class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None 
    def is_empty(self):
        return self.front == None 
    def enqueue(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.rear = self.front = new_node
            return 
        self.rear.next = new_node
        self.rear = new_node
    def display(self):
        if not self.is_empty():
            temp = self.front
            while temp :
                print(temp.data,end='=>')
                temp = temp.next 
    def peak(self):
        if not self.is_empty():
            return self.front.data
        print('queue is empty')
    def dequee(self):
        if self.is_empty():
            print('queue is already empty')
            return 
        element = self.front.data
        if self.front == None:
            self.front = self.rear = None
        self.front = self.front.next
        return element
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(100)
q.dequee()
q.dequee()
q.dequee()
q.display()

class CircularQueue:
    def __init__(self):
        self.size = 3
        self.array = [None]*self.size
        self.front = -1
        self.rear = -1 
    def is_empty(self):
        return self.front == -1 
    def is_full(self):
        return (self.rear+1)%self.size == self.front
    def enqueue(self,data):
        if self.is_full():
            print('queeu overflow condition')
            return 
        if self.is_empty():
            self.front += 1 
        self.rear = (self.rear + 1)%self.size
        self.array[self.rear] = data
    def dequeue(self):
        if self.is_empty():
            print('queue underflow condtion')
            return 
        remover = self.array[self.front]
        if self.front == self.rear :
            self.front = self.rear = -1 
        else :
            self.front = (self.front + 1) % self.size
        return remover
    def display(self) :
       if self.is_empty():
           print('queue is empty')
       else :
           i = self.front
           while True :
               print(self.array[i],end = ' ')
               if i == self.rear :
                   break 
               i = (i + 1)% self.size
           print()
           
c =CircularQueue()
c.enqueue(10)
c.enqueue(20)
c.dequeue()
c.enqueue(100)
c.enqueue(200)
c.enqueue(400)
c.display()     
        