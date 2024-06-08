//printing x
#include<stdio.h>
void main(){
  int size=10*10;
  for(int row=0;row<size;row++){
    for(int col=0;col<size;col++){
      if(row==col||(row+col)==size-1)
        printf("* ");
      else
        printf("  ");
    }
    printf("\n");
  }
}