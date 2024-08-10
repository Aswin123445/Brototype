class Array:
    def __init__(self,size,array):
       self.size=size
       self.array=array
    def input_data(self):
       for i in range(self.size):
          self.array[i]=int(input("data"))
    def output_data(self):
       #outputing data to the console
       for i in range(self.size):
          print(self.array[i])
size=int(input("enter the size of the array"))
#declaring list wit zero comprensation
list=[0 for i in range(size)]
array=Array(size,list)
array.input_data()
array.output_data()
