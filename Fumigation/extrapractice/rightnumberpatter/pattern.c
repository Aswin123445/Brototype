//printing numbers
#include<stdio.h>
void main(){
  int rows;
  printf("enter number of rows want\n");
  scanf("%d",&rows);
  //loop for rows
  for(int row=0;row<rows;row++){
    //printing number in each col
    
  int counter=rows-row+1;
    for(int num=0;num<(rows-row)*2-1;num++){
      if(counter>0&&num<=((rows-row)*2-1)/2){
        counter--;
        printf("%d ",counter);
      }
      else{
          counter++;
          printf("%d ",counter);
          
      }
    }
    printf("\n");
  }
}