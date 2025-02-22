class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if  self.is_empty():
            print('stack is empty')
            return
        self.stack.pop()
    def peak(self):
        return self.stack[-1]
    def display(self):
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i],end=" ")
        print()
    def push_no_duplicates(self,data):
        print('helo')
        if data in self.stack :
            print('values already in the list!')
            return
        else :
            self.stack.append(data)
            
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedStack:
    def __init__(self):
        self.stack = None
    def is_empty(self):
        return self.stack is None
    def push(self,data):
        new_node = Node(data)
        if not new_node :
            print('stack overflow condition')
            return 
        new_node.next = self.stack
        self.stack = new_node
    def pop(self):
        if self.is_empty() :
            print('stack underflow conditon')
            return
        ch = self.stack.data
        self.stack = self.stack.next
        return ch
        
    def display(self):
       if self.is_empty():
            print('stack is empty')
            return
       temp = self.stack
       while temp :
           print(temp.data,end='->')
           temp = temp.next
           
    def reverse(self,string):
        ch = ''
        #insert charcters to the linked list
        for i in string :
            self.push(i)
        
        #pop the element from the linked list
        while self.stack :
            ch += self.pop()
        return ch
    def palidrome_check(self,string):
        mid = len(string)//2
        for i in range(mid):
            self.push(string[i])
        #check whedher even or odd
        print(f'mid is {mid}')
        if (mid+1) % 2 == 1:
            print('hi')
            mid += 1
        #checking the elemnts

        while mid < len(string):
            if self.pop() != string[mid]:
                print('not palidrome')
                return False
            mid += 1
        print('it is a palidrome')

s = Stack()
s.push(10)
s.display()
s.push(30)
s.display()
s.pop()
s.display()
print(s.peak())
s.pop()
s.pop()
s.push_no_duplicates(10)
s.push_no_duplicates(10)
s.display()

print('end of era')
l = LinkedStack()
print(l.reverse('aswin'))
ll = LinkedStack()
ll.palidrome_check('malayalam')


