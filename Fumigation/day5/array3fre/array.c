#include<stdio.h>
void main(){
  int array[50],size;
  printf("enter size of array\n");
  scanf("%d",&size);
  //input elements of array
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //output entered elements
  printf("entered elements are\n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
  //finding elemets which their frequency is 3
  for(int index=0;index<size;index++){
    int fre=1;
    for(int index2=index+1;index2<size;index2++){
      if(array[index]==array[index2]){
         fre++;
         array[index2]=-1;
      }
    }
    if(fre==3&&array[index]!=-1)
      printf("\n%d has three times",array[index]);
  }
}