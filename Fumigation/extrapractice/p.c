#include<stdio.h>
void main(){
  int size,array[10];
  printf("enter size of array\n");
  scanf("%d",&size);
  //loop for rows
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
  }
  int left,right;
  left=right=0;
  while(right<size){
    if(array[right]<0){
      int temp=array[left];
      array[left]=array[right];
      array[right]=temp;
      left++;
    }
    if(array[right]<0)
     right++;
  }
  for(int index=0;index<size;index++){
    printf("%d ",array[index]);
  }
}
