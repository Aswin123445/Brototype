class CircularQueue:
    def __init__(self,cap):
        self.cap = cap
        self.queue = [None]*cap
        self.front = -1
        self.rear = -1
    def is_empty(self):
        return self.front == -1
    def is_full(self):
        return (self.rear+1)%self.cap == self.front
    def enqueue(self,data):
        if self.is_full():
            print('queue is alaready full')
            return
        if self.front == -1 :
            self.front = self.rear = 0
        else :
            self.rear = (self.rear+1)%self.cap
        self.queue[self.rear] = data
    def dequeue(self):
        if self.is_empty():
            print('underflow conditon reached')
            return None
        data = self.queue[self.front]
        if self.rear == self.front :
            self.front=self.rear=-1
        else :
            self.front = (self.front+1)%self.cap
        return data
    
    def display(self):
        if self.is_empty():
            print("list is empty")
            return
        i = self.front
        while i != self.rear :
            print(self.queue[self.front],end=' ')
            i = (i+1)%self.cap
        print(self.queue[self.rear])
        print()
        
c = CircularQueue(4)
c.enqueue(10)
c.enqueue(20)
c.display()
c.dequeue()
c.dequeue()
c.display()