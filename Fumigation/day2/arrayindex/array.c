//finding index of array
#include<stdio.h>
void main(){
  int array[10],size,num;
  printf("enter size of array\n");
  scanf("%d",&size);
  //input elements
  for(int index=0;index<size;index++){ 
    scanf("%d",&array[index]);
  }
  printf("enter number in the array want to find the index\n");
  scanf("%d",&num);
  for(int index=0;index<size;index++){
    if(num==array[index]){
      printf("element found at index :%d",index);
      break;
    }  
  }
}