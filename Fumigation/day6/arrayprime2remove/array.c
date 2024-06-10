#include<stdio.h>
#include<stdbool.h>
bool prime(int number){
  int count=2;
  while(count<number){
    if(number%count==0){
      return false;
    }
    count++;
  }
  return true;
}
void main(){ 
  int array[10],size;
  printf("enter size of array\n");
  scanf("%d",&size);
  //input elements of array
  printf("enter elements of array\n");
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //output entered elements
  printf("entered elements are\n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
  //deleting two elements after occurance prime number
  //traversal
  for(int index=0;index<size;index++){
    //checking prime number
    bool isPrime=prime(array[index]);
    if(isPrime){
      //removing next two elements
      int repeat=0;
      while(repeat<=1){
        for(int rem=index+1;rem<size-1;rem++){
          array[rem]=array[rem+1];
        }
        size--;
        repeat++;
      }
    }
  }
  printf("\n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
}