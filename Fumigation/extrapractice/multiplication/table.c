//Write a program to print the multiplication table of given number
#include<stdio.h>
void main(){
  int number;
  printf("enter the number you want to find the table\n");
  scanf("%d",&number);
  //loop to print the table
  for(int index=0;index<=10;index++){
    printf("%d * %d  = %d\n",index,number,index*number);
  }
}