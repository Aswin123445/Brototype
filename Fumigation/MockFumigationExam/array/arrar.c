//prime numbers and remplace with zero
#include<stdio.h>
#include<stdbool.h>
//function to find number prime or not
bool isPrime(int number){
  if(number==1) 
    return false;
  else{
    int count=2;
    while(count<number){
      if(number%count==0)
        return false;
      count++;
    }
  }
  return true;
}
void main(){
  int array[10],size;
  printf("enter size of array\n");
  scanf("%d",&size);
  //loop to input array
  printf("enter elements of array\n");
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //printint entered elements
  printf("entered elements are\n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
  //loop to find prime numbers
  for(int index=0;index<size;index++){
    //calling prime function
    bool checker=isPrime(array[index]);
    if(checker)
      array[index]=0;
  }
  //loop to print updated array elements
  printf("\n Updated array without prime number is \n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
}