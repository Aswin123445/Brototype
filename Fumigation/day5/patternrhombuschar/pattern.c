//rhombus star pattern
#include<stdio.h>
void main(){
  int rows;
  printf("enter rows of array\n");
  scanf("%d",&rows);
  //loop for rows
  int spaces=rows-1;
  for(int row=0;row<rows;row++){
    //loop for printing space in each row
    for(int space=0;space<spaces;space++)
      printf("  ");
    spaces--;
    //loop for printing stars
    char count='A';
    for(int star=0;star<rows;star++){
      printf("%c ",count);
      count++;
    }
    printf("\n");
  }
}