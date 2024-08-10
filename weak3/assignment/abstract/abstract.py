#to use abstract class in python we need to use extrenal module
#which is ABC and abstractmethod
from abc import ABC,abstractmethod
#creating an abstract class
class Calculator(ABC):
    @abstractmethod
    def do(self):
        pass
    
#classes which will override the abstract method
class Addition(Calculator):
    #method definition in this code
    def do(self):
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        return a+b
class Substract(Calculator):
    #method definition in this code
    def do(self):
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        return a-b
class Multiply(Calculator):
    #method definition in this code
    def do(self):
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        return a*b
class Division(Calculator):
    #method definition in this code
    def do(self):
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        return a/b
additon=Addition()
multiplication=Multiply()
division=Division()
substract=Substract()
print("Online Calculator")
value=int(input("press 1 for division \n press 2 for substraction \n press 3 for multiplication \n press 4 for additon"))
match value:
    case 1:
       print(division.do())
    case 2:
        print(substract.do())
    case 3:
        print(multiplication.do())
    case 4:
        print(additon.do())
    case _:
        print("invalid entry")