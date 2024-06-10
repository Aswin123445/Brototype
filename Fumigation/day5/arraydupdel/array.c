#include<stdio.h>
void main(){
  int array[50],size;
  printf("enter size of array\n");
  scanf("%d",&size);
  //input elements of array
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //output entered elements
  printf("entered elements are\n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
  //finding elemets which have duplicates
  for(int index=0;index<size;index++){
    int fre=1;
    for(int index2=0;index2<size;index2++){
      if(array[index]==array[index2]&&index!=index2){
         //removing duplicates
         for(int dup=index2;dup<size-1;dup++){
           array[dup]=array[dup+1];
         }
         size--;
      }
    }
  }
  printf("\n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
}