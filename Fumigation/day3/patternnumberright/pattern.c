#include<stdio.h>
void main(){
  int rows;
  printf("enter number of rows\n");
  scanf("%d",&rows);
  //printing rows
  int stars=rows;
  for(int row=0;row<rows;row++){
    //printing numbers
    int counter=1;
    for(int star=0;star<stars;star++){
      printf("%d ",counter);
      counter++;
    }
    stars--;
    printf("\n");
  }  
}