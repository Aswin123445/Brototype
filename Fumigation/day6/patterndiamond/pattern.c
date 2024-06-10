#include<stdio.h>
void main(){
  int rows;
  printf("enter number of rows must be odd\n");
  scanf("%d",&rows);
  //loop for rows
  for(int row=0;row<rows;row++){
    //loop for printing space
    if(row<=rows/2){
      for(int space=0;space<row;space++)
        printf(" ");
      //loop for stars
      for(int star=0;star<((rows/2+1)-row)*2-1;star++)
        printf("*");
     }
     else{
       for(int space=0;space<(rows-1)-row;space++)
       printf(" ");
       //printing stars
       for(int star=0;star<(row-(rows/2)+1)*2-1;star++)
       printf("*");
     }
    printf("\n");
  }
}