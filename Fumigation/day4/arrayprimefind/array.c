//finding prime numbers in a array
#include<stdio.h>
#include<stdbool.h>
void main(){
  int size,array[10];
  printf("enter size of the array\n");
  scanf("%d",&size);
  //input elemtents of array
  printf("enter elements of array\n");
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
  }
  //outputting entered elements
  printf("entered elements are\n");
  for(int index=0;index<size;index++){
    printf("%d ",array[index]);
  }
  printf("\nPrime numbers are ->");
  //printing prime number
  for(int index=0;index<size;index++){
    if(array[index]!=0){
      int checker=2;
      bool isprime=true;
      while(checker<array[index]/2+1){
        if(array[index]%checker==0){
          isprime=false;
          break;
        }else{
           checker++;
        }
      }
      if(isprime==true){
        printf("%d ",array[index]);
      }
    }
  }
}
