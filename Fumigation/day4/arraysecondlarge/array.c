//finding second largest elements in the array
#include<stdio.h>
void main(){
  int array[10],size,largest,slargest;
  printf("enter size of the array\n");
  scanf("%d",&size);
  //inputing elements of array
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  largest=slargest=array[0];
  //outputting entered elements
  printf("entered elemtents are \n");
  //finding second largest element
  for(int index=1;index<size;index++){ 
    if(array[index]>largest){
      slargest=largest;
      largest=array[index];
    }
  }
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
  printf("\nsecond largest element :%d",slargest);
}