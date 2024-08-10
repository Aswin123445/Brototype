#program to find the sum of multiple arguments passed to a funtion
def argument(*argv):
    sum=0
    for i in argv:
        sum+=i
    return sum
print(argument(1,2,3,4))
