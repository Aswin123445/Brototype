//printing star right angle pattern
#include<stdio.h>
void main(){ 
  int rows;
  printf("enter number of rows you want\n"); 
  scanf("%d",&rows);
  //loop for row
  for(int row=0;row<rows;row++){
    //loop to print stars in each line
    for(int star=0;star<=row;star++){
      printf("*");
    }
    printf("\n");
  }
}