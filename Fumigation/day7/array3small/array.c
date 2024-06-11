//find the third largest element without sorting
#include<stdio.h>
void main(){
  int array[10],size;
  printf("enter size of the array\n");
  scanf("%d",&size);
  //loop to input data
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //loop to output
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
  //finding third largest element
  int small,sSecond,sThird;
  small=sSecond=sThird=array[0];
  for(int index=1;index<size;index++){ 
    if(array[index]<small){
      sThird=sSecond;
      sSecond=small;
      small=array[index];
    }
    else if(array[index]<sSecond){
      sThird=sSecond;
      sSecond=array[index];
    }
  }
  printf("\n %d ",sThird);
}