#include<stdio.h>
void main(){
  int rows;
  printf("enter number of rows\n");
  scanf("%d",&rows);
  //printing rows
  int stars=rows;
  for(int row=0;row<rows;row++){
    //printing stars 
    for(int star=0;star<stars;star++){
      printf("*");
    }
    stars--;
    printf("\n");
  }  
}