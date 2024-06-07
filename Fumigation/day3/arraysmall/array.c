//program to find samllest element in array
#include<stdio.h>
void main(){
  int array[10],small,size;
  printf("enter size of the array\n");
  scanf("%d",&size);
  printf("please enter elements of the array\n");
  //inputing elements of array
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
  }
  small=array[0];
  //finding smallest element
  for(int index=1;index<size;index++){
    if(small>array[index])
       small=array[index];
  }
  printf("\n samllest element is:%d",small);
}