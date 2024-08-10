print("program to find the mathematical operation based on the user input")
print("please select from the given options\n 1 :addition  \n2: substraction  \n3:multiplication \n4:division")
option=int(input("please enter from the given option"))
is_continue=True
while(is_continue):
        match option:
           case 1:
              #additon
              print("enter two numbers")
              num1=int(input())
              num2=int(input())
              print("sum of number is {}".format(num1+num2))
           case 2:
           #substraction
              print("enter two numbers")
              num1=int(input())
              num2=int(input())
              print("sumbstraction of number is {}".format(num1-num2))
           case 3:
           #multiplication
               print("enter two numbers")
               num1=int(input())
               num2=int(input())
               print("product of number is {}".format(num1*num2))
           case 4:
           #division
               print("enter two numbers")
               num1=int(input())
               num2=int(input())
               print("division  of number is {}".format(num1/num2))
           case _:
               print("invalid expression has enetered please verify the input")
        str=input("do you want to coninue y or n")
        if(str=="n" or str=="N"):
           is_continue=False