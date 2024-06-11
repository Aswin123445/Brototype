#include<stdio.h>
void main(){ 
  int rows;
  printf("enter number of rows\n");
  scanf("%d",&rows);
  //loop for printing first rows
  for(int row=0;row<rows;row++){
    int count=0;
    //loop for number
    for(int number=0;number<rows-row;number++){
       printf("%d",++count);
    }
    //loop for printing stars;
    for(int star=0;star<(row)*2;star++){
      printf("*");
    }
    //loop for printing second number set
    int secondCounter=rows-row;
    for(int number=0;number<rows-row;number++){
      printf("%d",secondCounter--);
    }
    printf("\n");
  }
}