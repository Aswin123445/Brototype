#program to demo funtions and lamda funtions
#lamda funtion is specail funtion that number of arguments and one expression
#funtion to calculate the sum of two numbers
def sum_of_two(a):
   sum=lambda x:a+x
   return sum
number=int(input("enter number you want to add 100"))
lamp=sum_of_two(number)
print(lamp(100))
