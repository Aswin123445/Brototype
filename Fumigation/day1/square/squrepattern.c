#include<stdio.h>
void main(){
  int rows;
  printf("enter the rows you want\n");
  scanf("%d",&rows);
  //printing rows
  for(int row=0;row<rows;row++){
    //printing number of colums
    for(int col=0;col<rows;col++){
      printf("* ");
    }
    printf("\n");
  }
}