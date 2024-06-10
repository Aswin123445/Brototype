//finding average of prime numbers in array
#include<stdio.h>
#include<stdbool.h>
bool prime(int number){
  if(number==1)
    return false;
  int counter=2;
  while(counter<number){
    if(number%counter==0)
       return false;
    counter++;
  }
  return true;
}
int avg(int sum,int terms){
  int average=sum/terms;
  return average;
}
void main(){
  int array[10],size;
  printf("enter size of array\n");
  scanf("%d",&size);
  //inputing  elements to the array
  for(int index=0;index<size;index++)
    scanf("%d",&array[index]);
  //output entered elements
  printf("entered elements are\n");
  for(int index=0;index<size;index++)
    printf("%d ",array[index]);
  //finding average of prime numbers
  int sum=0,count=0;
  for(int index=0;index<size;index++){
    bool isPrime=prime(array[index]);
    if(!isPrime){
      sum+=array[index];
      count++;
    }
  }
  int avgerage=avg(sum,count);
  printf("\n%d ",avgerage);
}