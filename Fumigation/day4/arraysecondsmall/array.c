//finding second smallest number
#include<stdio.h>
void main(){
  int array[10],size,small,sSmall;
  printf("enter size of array\n");
  scanf("%d",&size);
  //inputing elements to the array
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //finding second smallest element
  small=array[0];
  sSmall=array[1];
  for(int index=1;index<size;index++){
    if(array[index]<small){
      sSmall=small;
      small=array[index];
    }
  }
  //printing entered elements
  printf("entered elements are\n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
  printf("\nsecond smallest element is :%d",sSmall);
}