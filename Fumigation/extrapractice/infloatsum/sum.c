//Accept two inputs from the user and output its sum.
#include<stdio.h>
void main(){
  int num1;
  float num2;
  printf("please enter the first number it must be an integer!\n");
  scanf("%d",&num1);
  printf("enter the second number and it must be an floating point number !\n");
  scanf("%f",&num2);
  printf("The sum of the number is\n");
  printf("%f",num1+num2);
}