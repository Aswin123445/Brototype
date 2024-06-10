#include<stdio.h>
void main(){
  int rows;
  printf("enter number of rows\n");
  scanf("%d",&rows);
  //loop for rows
  for(int row=0;row<rows;row++){ 
    //loop for cols
    char count='@';
    for(int col=0;col<rows;col++){
      if(row==0||row==(rows-1)||col==0|col==(rows-1)){
        printf("%c ",++count);
      }
      else{
        printf("  ");
        ++count;
      }
    }
    printf("\n");
  }
}