#include<stdio.h>
#include<stdbool.h>
//function to find prime number
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
    return true;
  }
}
void main(){
  int array[10],size;
  printf("enter size of array\n");
  scanf("%d",&size);
  //loop for inputing data
  printf("enter elements of array\n");
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //outputting entered elements
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
  //loop to delete element after occurance of non prime
  for(int index=0;index<size;index++){
    bool prime=isPrime(array[index]);
    if(!prime){
      //deleting three elemets
      int checker=0;
      while(checker<3){
        int del;
        for( del=index+1;del<size-1;del++){
          array[del]=array[del+1];
        }
        if(del<size)
        size--;
        checker++;
      }
    }
  }
  printf("\n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
}