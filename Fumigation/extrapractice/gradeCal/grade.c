//telling the grade after user entering their total marks
#include<stdio.h>
void main(){
  int markPer;
  printf("enter mark percentage of the student\n");
  scanf("%d",&markPer);
  if(markPer>100||markPer<0){
    printf("Invalid entry\n");
    return;
  }else{
    if(markPer<50)
      printf("Student failed in the exam\n");
    else if(markPer<60)
      printf("Student grade is  :E\n");
    else if(markPer<70)
      printf("Student grade is  :D\n");
    else if(markPer<80)
      printf("Student grade is  :C\n");
    else if(markPer<90)
      printf("Student grade is  :B\n");
    else
      printf("Student grade is  :A\n");
  }
}