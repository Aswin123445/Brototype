class StringStack:
    def __init__(self):
        self.stack =[]
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        string = ''
        if self.is_empty():
            print('stack is empyt')
            return
        return  self.stack.pop()
    #finding palidrome or not
    def palidrome(self,data):
        mid = int(len(data)/2)
        #push operation
        i = 0
        while i < mid :
            self.push(data[i])
            i += 1
        if len(data) % 2 == 1:
            i += 1
        #poping elemnents
        print(len(data))
        print(self.stack)
        while i < len(data):
            if self.pop() != data[i]:
                return
            i+=1  
        print('string is palidrome')  
s = StringStack()
# string = input("enter the string want to reverse")

# #pushing to the string
# for i in string:
#     s.push(i)
    
# #poping the pushed the characters
# char = ''
# for i in range(len(s.stack)):
#     char += s.pop()
    
# print(char)

s.palidrome('malayalam')