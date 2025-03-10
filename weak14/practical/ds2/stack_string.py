# class StringStack:
#     def __init__(self):
#         self.stack =[]
#     def is_empty(self):
#         return len(self.stack) == 0
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         string = ''
#         if self.is_empty():
#             print('stack is empyt')
#             return
#         return  self.stack.pop()
#     #finding palidrome or not
#     def palidrome(self,data):
#         mid = int(len(data)/2)
#         #push operation
#         i = 0
#         while i < mid :
#             self.push(data[i])
#             i += 1
#         if len(data) % 2 == 1:
#             i += 1
#         #poping elemnents
#         print(len(data))
#         print(self.stack)
#         while i < len(data):
#             if self.pop() != data[i]:
#                 return
#             i+=1  
#         print('string is palidrome')  
# s = StringStack()
# # string = input("enter the string want to reverse")

# # #pushing to the string
# # for i in string:
# #     s.push(i)
    
# # #poping the pushed the characters
# # char = ''
# # for i in range(len(s.stack)):
# #     char += s.pop()
    
# # print(char)

# s.palidrome('malayalam')

#implementing stack using linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Stack:
    def __init__(self):
        self.head = None 
    def push(self,data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return 
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.head is None:
            self.head = None 
            return 
        data = self.head.data
        self.head = self.head.next
        return data
    def peak(self):
        if self.head is not None :
            return self.head.data
            
    def display(self):
        if self.head == None :
            return 
        temp = self.head
        while temp:
            print(temp.data,end= ' ')
            temp = temp.next
        print() 
        
#implementation using bytearray
class ArrayStack:
    def __init__(self):
        self.array = []
    def is_empty(self):
        return len(self.array) == 0
    def push(self,data):
        self.array.append(data)
    def pop(self):
        if self.is_empty():
            return None
        data = self.array.pop()
        return data
    def peak(self):
        if not  self.is_empty():
          return self.array[-1]
    def display(self):
        for i in range(len(self.array)-1,-1,-1):
            print(self.array[i],end= " ")
        print()
            
#parandhesis checking
def is_parandhesis(string):
    pp = ArrayStack()
    phairs = {')':'(','}':'{',']':'['}
    for char in string :
        if char in phairs.values():
            pp.push(char)
            
        elif char in phairs.keys():
          if pp.is_empty() or pp.pop() != phairs.get(char,None):
            return False
    return pp.is_empty()
    
#reverse a string in stack 
def reverse_string(string):
    st = ArrayStack()
    reverse = ''
    for char in string:
        st.push(char)
    while not st.is_empty():
        reverse += st.pop()
    return reverse
    
#checking palicrome or not 
def palidrome(string):
    mid = len(string)//2 
    ss = ArrayStack()
    for i in range(mid):
        ss.push(string[i])
    if len(string)%2 == 1 :
        mid += 1
    while mid < len(string) :
        if string[mid] != ss.pop():
            return False
        mid+=1
    return True

#sort a stack 
    
    
            
        
    
s = ArrayStack()
s.push(10)
s.push(100)
s.push(200)
s.push(300)
s.push(250)
s.push(50)
s.push(20)

s.pop()
print(s.peak())
s.display()

a = ArrayStack()
a.push(10)
a.push(20)
a.display()

man='{(){}}'
print(reverse_string('manojkumar'))
print(palidrome('ardra'))
print(is_parandhesis(man))

def sort_stack(stack):
    temp_stack = ArrayStack()
    while stack.array:
       temp = stack.pop()
       while  temp_stack.array and temp_stack.peak() > temp :
           stack.push(temp_stack.pop())
       temp_stack.push(temp)
       #insert
    while temp_stack.array :
        stack.push(temp_stack.pop()) 
sort_stack(s)
s.display()
        
