//deleting element from array
#include<stdio.h>
void main(){
  int array[10],size,pos;
  printf("enter size of the array\n");
  scanf("%d",&size);
  //inputing elements of array
  printf("enter elements of the array\n");
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //outputting element
  for(int index=0;index<size;index++)
    printf("%d\t",array[index]);
  //inputing the position want to delete
  printf("enter position you want to delete\n");
  scanf("%d",&pos);
  //deleting the element
  for(int index=pos-1;index<size-1;index++){
    array[index]=array[index+1];
  }
  size--;
  //printing deleted array
  for(int index=0;index<size;index++)
    printf("%d\t",array[index]);
}
