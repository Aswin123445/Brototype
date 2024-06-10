#include<stdio.h>
void main(){
  int rows;
  printf("enter number of rows in odd\n");
  scanf("%d",&rows);
  //loop for rows
  for(int row=0;row<rows;row++){
    int count=0;
    if(row<=rows/2){
      //loop for star
      for(int star=0;star<=row;star++)
        printf("%d ",++count);
    }
    else{
      //loop for star
      for(int star=0;star<(rows-row);star++)
        printf("%d ",++count);
    }
    printf("\n");
  }
}