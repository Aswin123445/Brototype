#include<stdio.h>
void main(){
  int rows;
  printf("enter number of rows\n");
  scanf("%d",&rows);
  //printing rows
  int spaces=rows-1;
  for(int row=0;row<rows;row++){
    //printing space 
    for(int space=0;space<spaces;space++)
      printf("  ");
    spaces--;
    //printing stars 
    int count=1;
    for(int stars=0;stars<(row+1)*2-1;stars++){
      printf("%d ",count);
      count++;
    }
    printf("\n");
  }  
}