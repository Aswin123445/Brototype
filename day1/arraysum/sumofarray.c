#include<stdio.h>
void main(){ 
  //calculating sum of the array
  int array[20],sum=0,size;
  printf("enter size of the array\n");
  scanf("%d",&size);
  printf("enter the elements of the array\n");
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
     sum=sum+array[index];
  }
  //printing the entered array
  for(int index=0;index<size;index++)
    printf("%d\t",array[index]);
  printf("\n the sum of array is \t:%d",sum);
}