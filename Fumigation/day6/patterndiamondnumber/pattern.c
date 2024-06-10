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
      int counter=0;
      for(int count=0;count<((rows/2+1)-row)*2-1;count++)
        printf("%d",++counter);
     }
     else{
       for(int space=0;space<(rows-1)-row;space++)
       printf(" ");
       //printing stars
       int counter=0;
       for(int count=0;count<(row-(rows/2)+1)*2-1;count++)
       printf("%d",++counter);
     }
    printf("\n");
  }
}