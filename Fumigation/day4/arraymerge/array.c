//merge two arrays into third array
#include<stdio.h>
void main(){
  int array[10],array2[10],array3[20],size1,size2,size3;
  printf("size of first array\n");
  scanf("%d",&size1);
  printf("size of second array\n");
  scanf("%d",&size2);
  size3=size1+size2;
  int count=0;
  //inuting elements of both array
  printf("enter elemtents of first array\n");
  for(int arrayOneIndex=0;arrayOneIndex<size1;arrayOneIndex++){
    scanf("%d",&array[arrayOneIndex]);
  }
  printf("enter elements of second array\n");
  for(int arrayTwoIndex=0;arrayTwoIndex<size2;arrayTwoIndex++){
    scanf("%d",&array2[arrayTwoIndex]);
  }
  //merging both array
  for(int arrayThreeIndex=0;arrayThreeIndex<size3;arrayThreeIndex++){
    if(arrayThreeIndex<size1)
       array3[arrayThreeIndex]=array[arrayThreeIndex];
    else{
       array3[arrayThreeIndex]=array2[count];
       count++;
    }
  }
  //printing both array merged array
  for(int arrayThreeIndex=0;arrayThreeIndex<size3;arrayThreeIndex++){
    printf("%d ",array3[arrayThreeIndex]);
  }
}