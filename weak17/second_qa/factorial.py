#factorial of a number 
def fact(number):
    if number > 0:
      return number * fact(number-1)
    else :
        return 1
  
print(fact(5))