//Hollow square star pattern with diagonal
#include<stdio.h>
void main(){ 
  int rows;  
  printf("enter rows you want to print stars\n");
  scanf("%d",&rows);
  //loop for rows
  for(int row=0;row<rows;row++){ 
    //printing colums
    for(int col=0;col<rows;col++){
      if(row==0||row==rows-1||col==0||col==rows-1||col==row||(col+row)==(rows-1))
        printf("* ");
      else
        printf("  ");
    }
    printf("\n");
  }
}