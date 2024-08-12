# def fact(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         for i in range(1,num+1):
#             fact=fact*i
#             #1*2*3*
def pattern(size):
    for row in range(size):
       for col in range(size-row):
           print("*",end=" ")
       print("\n")

pattern(5)