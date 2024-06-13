//interchanging values of two array
#include<stdio.h>
void main()
{
  int array[5]={10,20,30,40,50};
  int array2[5]={100,200,300,400,500};
  //interchanging values
  for(int index=0;index<5;index++){
    int temp1=array[index];
    array[index]=array2[index];
    array2[index]=temp1;
  }
  for(int index=0;index<5;index++){
    printf("%d  %d \n",array[index],array2[index]);
  }
}
