//pirint x pattern
#include<stdio.h>
void main(){
  //taking number of rows
  int rows;
  printf("enter number of rows it must be an odd number\n");
  scanf("%d",&rows);
  int firstV=rows/2+1;
  //printing to rows
  int secondSpace=(firstV-1)*2-1;
  for(int row=0;row<firstV;row++){
    //printing first spaces
    for(int space=0;space<row;space++){
      printf(" ");
    }
    //pirntfing first star
    printf("*");
    //printing second set of spaces
    for(int space=0;space<secondSpace;space++){
      printf(" ");
    }
    secondSpace=secondSpace-2;
    //printing remaining stars
    if(row!=firstV-1)
      printf("*");
    printf("\n");
  }
  //printing the second rows
  int secondV=rows-firstV;
  int sSpace=secondV-1;
  for(int row=0;row<secondV;row++){
    //printing space;
    for(int space=0;space<sSpace;space++){
      printf(" ");
    }
    sSpace--;
    //printing first *
    printf("*");
    //printing inner space
    for(int space=0;space<(row+1)*2-1;space++){
      printf(" ");
    }
    //printing star
    printf("*");
    printf("\n");
  }
}