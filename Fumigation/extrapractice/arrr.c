#include<stdio.h>
void main(){
  int array[10],size;
  printf("size\n");
  scanf("%d",&size);
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //finding multiple of 3
  int end=size-1;
  for(int index=0;index<size;index++){
    if(array[index]%3==0){
      int temp=array[index];
      array[index]=arr[end];
      array[end]=temp;
      end--;
    }
    if(array[index]%2==0){
      for(int del=index;del<size-1;del++)
        array[del]=array[del+1];
      size--;
    }
  }
  for(int index=0;index<size;index++){
    printf("%d ",array[index]);
  }
}