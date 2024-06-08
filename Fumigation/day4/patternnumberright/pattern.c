//pattern coding
#include<stdio.h>
void main(){
  int rows;
  printf("enter number of rows\n");
  scanf("%d",&rows);
  //printing loop for rows
  for(int row=0;row<rows;row++){
    //printing loop for spaces
    for(int space=0;space<row;space++)
      printf("  ");
    //loop for stars
    int counter=1;
    for(int number=0;number<(rows-row);number++){
      printf("%d ",counter);
      counter++;
    }
    printf("\n");
  }
}