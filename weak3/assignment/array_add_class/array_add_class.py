class ArrayAddition:
    def __init__(self,size,list,list1,result):
        self.size=size
        self.list=list
        self.list1=list1
        self.result=result
    def inputelements(self,):
        
        for i in range(self.size):
            for j in range(self.size):
                self.list[i][j]=int(input())
    def inputelements1(self):
        
        for i in range(self.size):
            for j in range(self.size):
                self.list1[i][j]=int(input())
    def displaying_elements(self):
        for i in range(self.size,):
            for j in range(self.size):
                print(self.list[i][j])

    def addingelements(self):
        for i in range(self.size):
            for j in range(self.size):
                self.result[i][j]=self.list[i][j]+self.list1[i][j]
    def displaying_result(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.result[i][j])
            print(end="\n")
size=int(input("enter size to an array"))
list=[[0]*2 for i in range(2)]
list2=[[0]*2 for i in range(2)]
result=[[0]*2 for i in range(2)]
arr=ArrayAddition(size,list,list2,result)
print("inputing elements")
arr.inputelements()
print("displaying other set of array")
arr.inputelements1()
print("displaying elements")
arr.displaying_elements()
print("adding elements")
arr.addingelements()
print("displaying result")
arr.displaying_result()

    