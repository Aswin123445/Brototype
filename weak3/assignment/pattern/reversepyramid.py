#in this program we are going to print a pattern that increaments it's value form
#right side 
size=int(input("enter length of the pattern"))
counter=1
for i in range(0,size):
    for j in range(size-i):
        counter=counter+1
iterator=counter
#for loop for rows
for row in range(size):
    counter=counter-(size-row)
    cheker=counter
    for col in range(size-row):
        print(cheker,end=" ")
        cheker=cheker+1
    print(end="\n")
    