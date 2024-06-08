#include<stdio.h>
void main(){
  int rows;
  printf("enter total rows want \n");
  scanf("%d",&rows);
  //loop for rows
  for(int row=0;row<rows;row++){
    //loop for printing spaces in each row
    for(int space=0;space<row;space++)
      printf("  ");
    char count='@';
    //loop for printing stars
    for(int star=0;star<(rows-row)*2-1;star++)
      printf("%c ",++count);
    printf("\n");
  }
}