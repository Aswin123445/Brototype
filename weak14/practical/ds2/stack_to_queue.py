class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enque(self,data):
        self.stack1.append(data)
        
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return None
    
s = StackQueue()
s.enque(10)
s.enque(20)
s.enque(30)
print(s.dequeue())
print(s.dequeue())
