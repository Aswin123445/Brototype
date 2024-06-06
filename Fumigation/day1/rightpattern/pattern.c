#include<stdio.h>
//hollow right angle triangle
void main(){
  //inputing the rows
  int rows;
  printf("enter the rows of the pattern\n");
  scanf("%d",&rows);
  //loop for rows
  int outSpace=rows-1;
  for(int row=0;row<rows;row++){
    //print outerspaces
    for(int space=0;space<outSpace;space++){
      printf(" ");
    }
    outSpace--;
    //printing firstStars
    printf("*");
    //printing remaining pattern
    if(row>0){
      for(int col=0;col<=row-1;col++){
        if(row==rows-1||col==row-1)
          printf("*");
        else
          printf(" ");
      }
    }
    printf("\n");
  }
}