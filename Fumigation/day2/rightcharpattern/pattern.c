//printing alphabhets right angle pattern
#include<stdio.h>
void main(){ 
  int rows;
  printf("enter number of rows you want\n"); 
  scanf("%d",&rows);
  //loop for row
  for(int row=0;row<rows;row++){
    //loop to print number in each line
    char character='A';
    for(int number=0;number<=row;number++){
      printf("%c ",character);
      character++;
    }
    printf("\n");
  }
}