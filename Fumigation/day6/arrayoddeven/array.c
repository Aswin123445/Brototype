//seperte odd numbers and even numbers to separate array
#include<stdio.h>
void main(){
  int array[10],array1[10],array2[10],size1,size2=0,size3=0;
  printf("enter size of array\n");
  scanf("%d",&size1);
  //inputing data
  printf("enter elements of array\n");
  for(int index=0;index<size1;index++)
    scanf("%d",&array[index]);
  //output data
  for(int index=0;index<size1;index++)
    printf("%d ",array[index]);
  //sorting even and odd
  for(int index=0;index<size1;index++){
    if(array[index]%2==0){
      array1[size2]=array[index];
      size2++;
    }else{
      array2[size3]=array[index];
      size3++;
    }
  }
  printf("\n");
  //printing odd and even array;
  for(int index=0;index<size2;index++)
    printf("%d ",array1[index]);
  printf("\n");
  for(int index=0;index<size3;index++)
    printf("%d ",array2[index]);
  
}