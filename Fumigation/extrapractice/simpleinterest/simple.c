//simple interest calculation
//formula is (P*I*N/100)
#include<stdio.h>
void main(){
  int principal,year;
  float ir,si;
  printf("enter Principal amount ,year of investment and rate of interest");
  scanf("%d",&principal);
  scanf("%d",&year);
  scanf("%f",&ir);
  si=year*ir/100*principal;
  printf("Interest amount for the given amount will be\t :%f",si);
}