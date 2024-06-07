//insert elements in the specific positions in the array
#include<stdio.h>
void main(){ 
  int array[15],size,pos,number;
  printf("enter size of the array\n");
  scanf("%d",&size);
  //inputing array elements
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //printing entered elements
  for(int index=0;index<size;index++)
    printf("%d\t",array[index]);
  printf("\nenter element you want to add");
  scanf("%d",&number);
  printf("\nenter position were you want to add");  
  scanf("%d",&pos);
  size++;
  //moving the posion of array til position mentioned
  for(int index=size-1;index>=pos;index--){
    array[index]=array[index-1];
  }
  array[pos-1]=number;
  //printing ubdated array
  for(int index=0;index<size;index++)
    printf("%d\t",array[index]);
}