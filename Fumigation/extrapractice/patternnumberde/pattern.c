#include<stdio.h>
void main(){
  int rows;
  printf("enter rows want to print\n");
  scanf("%d",&rows);
  //loop for rows
  int count=0;
  for(int row=0;row<rows;row++){
    if(row%2==0){
      for(int num=0;num<=row;num++){
        count++;
        printf("%d ",count);
      }
    }
    else{
      count=count+(row+1);
      for(int num=0;num<=row;num++){
        printf("%d ",count);
        count--;
      }
      count+=2;
    }
    printf("\n");
  }
}