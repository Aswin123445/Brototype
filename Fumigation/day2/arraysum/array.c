//program to calculate array sum
#include<stdio.h>
void main(){
  int array[10],size,sum=0;
  printf("enter size of the array\n");
  scanf("%d",&size);
  printf("please enter elements of the array\n");
  //inputing elements of array
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
    //calculating sum
    sum+=array[index];
  }
  //printing the inputed array and sum of array
  for(int index=0;index<size;index++)
    printf("%d\t",array[index]);
  printf("\n sum of array is  :%d",sum);
}