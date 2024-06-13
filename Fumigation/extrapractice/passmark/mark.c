//student passed or failed
#include<stdio.h>
#include<stdbool.h>
void main(){
  int mark;
  char ch;
  const int  passMark=50;
  bool isTrue=true;
  while(isTrue){
    printf("enter the mark of student\n");
    scanf("%d",&mark);
    if(mark>passMark)
      printf("student passed in the subject with %d percentage marks\n",mark);
    else
      printf("student failed in the subject with %d percentage marks\n",mark);

    printf("press 'y' to check result of other subject\n");
    scanf(" %c",&ch);

    isTrue=(ch=='y');
  }
}