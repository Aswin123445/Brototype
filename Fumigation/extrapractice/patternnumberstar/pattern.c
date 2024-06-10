#include<stdio.h>
void main(){
  int rows;
  printf("enter rows in odd number\n");
  scanf("%d",&rows);
  //loop for rows
  for(int row=0;row<rows;row++){
    int count=0;
    //printing stars in upper part
    if(row<=rows/2){
      for(int star=0;star<(row+1)*2-1;star++){
        if(star==0||star==(row+1)*2-2)
          printf("*");
        else if(star<((row+1)*2-1)/2+1){
          printf("%d",++count);
        }
        else
          printf("%d",--count);
      }
    }
    //printing lower stars
    else{
      for(int star=0;star<(rows-row)*2-1;star++){
        if(star==0||star==(rows-row)*2-2)
          printf("*");
        else if(star<((rows-row)*2-1)/2+1){
          printf("%d",++count);
        }
        else
          printf("%d",--count);
      }
    }
    printf("\n");
  }
}