class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0 
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
    def display(self):
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i],end=" ")
        print()
    def push(self,data):
        self.stack.append(data)
    def pop (self):
        return self.stack.pop()
        
    def sort(self):
        temp_stack = Stack()
        while not self.is_empty():
            temp = self.pop()
            while not temp_stack.is_empty() and temp < temp_stack.peak() :
                self.push(temp_stack.pop())
            temp_stack.push(temp)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack2:
    def __init__(self):
        self.stack = None
    def is_empty(self):
        return self.stack is None
    def push(self,data):
        new_node = Node(data)
        if not new_node:
            print('stack overflow conditon')
            return
        new_node.next = self.stack
        self.stack = new_node
        return
    def display(self):
        temp = self.stack
        if not temp :
            print('stack is empty')
            return
        while temp is not None:
            print(temp.data,end="->")
            temp =  temp.next
        print()
    def pop(self):
        self.stack = self.stack.next
    def peak(self):
        if not self.stack:
            print('stack is empyt')
            return None
        return self.stack.data
    def push_no_duplicates(self,data):
        new_node = Node(data)
        temp = self.stack
        while temp :
            if temp.data == data :
                print('data alredy in the stack')
                return
            temp = temp.next
        new_node.next = self.stack
        self.stack = new_node

s = Stack()
s.push(10)
s.display()
s.push(20)
s.display()
s.push(100)
s.display()
ss = Stack2()
ss.push(20)
ss.push(1)
ss.display()
ss.pop()
ss.display()
ss.push(200)
ss.push_no_duplicates(200)
ss.push_no_duplicates(30)
print(ss.peak())

print('helo')
s.display()
s.sort()
s.display()

