//finding unique elements in array
#include<stdio.h>
#include<stdbool.h>
void main(){
  int array[10],size;
  printf("enter size of array\n");
  scanf("%d",&size);
  //inputing data
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
  }
  //outputting elements
  for(int index=0;index<size;index++){
    printf("%d ",array[index]);
  }
  //finding unique elements
  for(int index=0;index<size;index++){
    bool isUnique=true;
    for(int index2=0;index2<size;index2++){
      if((array[index]==array[index2])&&index2!=index){
        isUnique=false;
        break;
      }
    }
    if(isUnique==true)
      printf("\n %d is unique",array[index]);
  }
}