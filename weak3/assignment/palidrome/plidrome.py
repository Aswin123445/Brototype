palidrome=input("enter a string")
start=0
end=len(palidrome)-1
isbool=True
while(start<end):
    if(palidrome[start]==palidrome[end]):
      isbool=True
    else:
      isbool= False
    end-=1
    start+=1
if(isbool):
   print("String is palidrome")
else:
   print("string is not palidrome")

