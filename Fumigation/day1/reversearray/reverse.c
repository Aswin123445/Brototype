//printing array in reverse order
#include<stdio.h>
void main(){
  int array[20],size;
  printf("enter the size of the array\n");
  scanf("%d",&size);
  printf("enter elements of the array\n");
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
  }
  //printing the entered elements of the array
  for(int index=0;index<size;index++){
    printf("%d\t",array[index]);
  }
  printf("\n");
  //printing the array in reverse order 
  for(int index=size-1;index>=0;index--)
    printf("%d\t",array[index]);   
}