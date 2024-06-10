#include<stdio.h>
void main(){
  int rows;
  int spaces=0;
  printf("enter number of rows\n");
  scanf("%d",&rows);
  //loop for rows
  for(int row=0;row<rows;row++){
    if(row<=rows/2){
      //loop for printing space
      for(int space=0;space<(rows/2)-row;space++)
        printf("  ");
      //loop for printing stars
      int count=0;
      for(int star=0;star<(row+1)*2-1;star++)
        printf("%d ",++count);
    }
    else{
      spaces++;
      //loop for printing space
      for(int space=0;space<spaces;space++)
        printf("  ");
      //loop for printing stars
      int count=0;
      for(int star=0;star<(rows-row)*2-1;star++)
        printf("%d ",++count);
    }
    printf("\n");
  }
}