//swich case day finder
#include<stdio.h>
void main(){ 
  int day;
  printf("enter the number of day you want to print\n");
  scanf("%d",&day);
  switch(day){
    case 1:
      printf("the day is sunday\n");
      break;
    case 2:
      printf("the day is Monday\n");
      break;
    case 3:
      printf("the day is Tuesday\n");
      break;
    case 4:
      printf("the day is Wednesday\n");
      break;
    case 5:
      printf("the day is Thusday\n");
      break;
    case 6:
      printf("the day is Friday\n");
      break;
    case 7:
      printf("the day is Saturday\n");
    default:
      printf("invalid input\n");
      break;
    
  }
}