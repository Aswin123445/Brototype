class Queue:
    def __init__(self,cap):
        self.queue = [None]*cap
        self.cap = cap
        self.front = -1
        self.rear = -1
        
    def is_empty(self):
        return self.front == -1
    def is_full(self):
        return self.rear == self.cap-1
    def enqueue(self,data):
        if self.is_full():
            print('overflow conditon')
            return
        if self.is_empty():
            self.front+=1
        self.rear += 1
        self.queue[self.rear] = data
    
    def dequeue(self):
        if self.is_empty():
            print('underflow conditon ')
            return
        element = self.queue[self.front]
        if self.front == self.rear :
            self.front = self.rear = -1
        else :
            self.front += 1
        return element
    
    def display(self):
        if not self.is_empty():
            print(self.queue[self.front:self.rear+1])
            
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front == None
    def enqueue(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.is_empty():
            print('queue is already empty return')
            return
        element = self.front.data
        if self.front.next is None :
            self.front = self.rear = None
        else :
            self.front = self.front.next
        return element
    def display(self):
        if not self.is_empty():
            temp = self.front
            print(temp.data)
            while temp:
                print(temp.data,end='->')
                temp=temp.next
        print()
            
q = Queue(4)
q.enqueue(10)
q.display()
q.enqueue(300)
q.display()
q.enqueue(100)
q.display()
q.enqueue(300)
q.display()
q.enqueue(40)
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()

s = LQueue()
s.enqueue(10)
s.enqueue(30)
s.display()
s.dequeue()
s.display()
s.enqueue(200)
s.display()

