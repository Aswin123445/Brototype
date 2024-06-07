//calculate average of all odd elemetns in the array
//formula for average sum/number of elements
#include<stdio.h>
void main(){
  int array[10],size,sum=0,oddCount=0;
  float avg;
  printf("enter size of the array\n");
  scanf("%d",&size);
  printf("please enter elements of the array\n");
  //inputing elements of array
  for(int index=0;index<size;index++){
    scanf("%d",&array[index]);
    if(array[index]%2!=0){
      sum+=array[index];
      oddCount++;
    }
  }
  avg=sum/oddCount;
  printf("\n average of array is :%f",avg);
}