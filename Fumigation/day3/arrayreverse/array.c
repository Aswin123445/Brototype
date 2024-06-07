//Reverse the elements of the array
#include<stdio.h>
void main(){
  int array[10],size;
  int startIndex=0,endIndex;
  printf("enter size of the array\n");
  scanf("%d",&size);
  endIndex=size-1;
  printf("please enter elements of the array\n");
  //inputing elements of array
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
  }
  while(startIndex!=endIndex){
    int temp=array[startIndex];
    array[startIndex]=array[endIndex];
    array[endIndex]=temp;
    startIndex++;
    endIndex--;
  }
  //printing reversed array
  for(int index=0;index<size;index++){
    printf("%d\t",array[index]);
  }
}