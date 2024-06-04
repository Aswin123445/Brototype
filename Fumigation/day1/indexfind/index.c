//printing index of the array
#include<stdio.h>
void main(){ 
  int array[20],size, element;
  printf("enter size of the array\n");
  scanf("%d",&size);
  printf("enter the elements of the array\n");
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
  }
  printf("please enter the element you want to check index\n");
  scanf("%d",&element);
  int checker=1;
  for(int index=0;index<size;index++){
    if(element==array[index]){
       checker=0;
       printf("element found in index  %d",index);
       break;
    }
  }
  if(checker==1)
    printf("\nentered number is not in the array\n");
  
}