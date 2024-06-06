//printing array in desending order
#include<stdio.h>
void main(){ 
  int array[10],size;
  printf("enter the size of the array\n");
  scanf("%d",&size);
  printf("enter elements of the array\n");
  //loop to input elements
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
  }
  //outpting elements
  for(int index=0;index<size;index++)
    printf("%d\t",array[index]);
  //sorting elemtents
  for(int index=0;index<size;index++){
    for(int checker=index+1;checker<size;checker++){
      if(array[index]<array[checker]){
        int temp=array[index];
        array[index]=array[checker];
        array[checker]=temp;
      }
    }
  }
  printf("\n");
  //printing the sorted array
    for(int index=0;index<size;index++)
    printf("%d\t",array[index]);
}