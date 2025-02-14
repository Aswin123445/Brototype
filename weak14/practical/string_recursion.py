class String:
    def __init__(self,word):
        self.word = word
    def reverse(self,sentance):
        if sentance == "" :
            return sentance
        return self.reverse(sentance[1:]) + sentance[0]
    def palidrome(self,sentance):
        print(f'{sentance} -> {len(sentance)}')
        if len(sentance) == 0 or len(sentance) == 1 :
            return True
        if sentance[0] == sentance[-1]:
            return self.palidrome(sentance[1:-1])
        return False
    
class Digit:
    def __init__(self,digit):
        self.digit = digit
    def digit_binary(self,digit):
        if digit == 0 or digit == 1 :
            return str(digit)
        return self.digit_binary(digit//2) + str(digit%2)
    
class Array:
    def __init__(self,array):
        self.array = array
    def binary_search(self,arr,left,right,data):
        if left > right :
            return None
        mid = int((left+right)/2)
        if arr[mid] == data:
            return mid
        if data>arr[mid]:
            return self.binary_search(arr,mid+1,right,data)
        return self.binary_search(arr,left,mid-1,data)
        
        
        
d= Digit(10)
li = d.digit_binary(d.digit)
print(li)
s = String("ardra")
print(s.reverse(s.word))
print(s.palidrome(s.word))

bina = Array([10,20,30,40,50,60])
pos = bina.binary_search(bina.array,0,len(bina.array)-1,60)
print(f'{bina.array[pos]} ->{pos+1}')

        