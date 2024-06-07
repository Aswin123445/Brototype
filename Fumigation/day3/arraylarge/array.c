//program to calculate array sum
#include<stdio.h>
void main(){
  int array[10],size,largest;
  printf("enter size of the array\n");
  scanf("%d",&size);
  printf("please enter elements of the array\n");
  //inputing elements of array
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);	
  }
  largest=array[0];
  //finding largest element
  for(int index=1;index<size;index++){
    if(array[index]>largest)
      largest=array[index];
  }
  printf("\n largest element is  :%d",largest);
}