#include<stdio.h>
void main(){
  int rows;
  printf("enter rows in the pattern\n");
  scanf("%d",&rows);
  int spaces=rows-1;
  //loop for rows
  for(int row=0;row<rows;row++){
    //loop for printing spaces
    for(int space=0;space<spaces;space++)
      printf(" ");
    spaces--;
    //printing rhombus
    for(int star=0;star<rows;star++){
      if(row==0||row==rows-1||star==0||star==rows-1)
        printf("* ");
      else
        printf("  ");
    }
    printf("\n");
  }
}