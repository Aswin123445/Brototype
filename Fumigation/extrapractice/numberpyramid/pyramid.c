//number pyramid
#include<stdio.h>
void main(){
  int rows;
  printf("enter the number of rows\n");
  scanf("%d",&rows);
  for(int row=0;row<rows;row++){
    //printing numbers
    int counter=1;
    for(int col=0;col<=row;col++){
      printf("%d",counter);
      counter++;
    }
    printf("\n");
  }
}