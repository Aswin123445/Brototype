#include<stdio.h>
void main(){
  int rows;
  printf("enter number of rows\n");
  scanf("%d",&rows);
  //loop for rows
  for(int row=0;row<rows;row++){
    int count=3
    //loop for triangle
    if(row<=rows/2){
      for(int num=0;num<=row;num++){
        printf("%d ",count);
      }
      count++;
    }
    else{
      count--;
      for(int num=0;num<(rows-row);row++){
        printf("%d ",count);
      }
    }
    printf("\n");
  }
}