//converting negative elements in the array to zero
#include<stdio.h>
void main(){
  int array[10],size;
  printf("enter the size of the array\n");
  scanf("%d",&size);
  //inputing elements of the array
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
  }
  //printing the elments user entered
  //removing negative numbers to zero (if any)
  for(int index=0;index<size;index++){
    printf("%d\t",array[index]);
    if(array[index]<0)
      array[index]=0;
  }
  printf("\n");
  //printing ubdated array
  for(int index=0;index<size;index++)
   printf("%d\t",array[index]);
}