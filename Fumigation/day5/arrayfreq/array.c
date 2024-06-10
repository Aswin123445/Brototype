//frequencu of elements in the array
#include<stdio.h>
void main(){
   int size,array[10];
   printf("enter size of array\n");
   scanf("%d",&size);
   printf("enter elements of array\n");
   for(int index=0;index<size;index++)
     scanf("%d",&array[index]);
   //printing entered elements
   for(int index=0;index<size;index++)
     printf("%d ",array[index]);
   //finding frequency of elements
   for(int index=0;index<size;index++){
     int frequency=1;
     for(int fre=index+1;fre<size;fre++){
       if(array[index]==array[fre]){
         frequency++;
         array[fre]=-1;
       }
     }
     if(array[index]!=-1)
       printf("\n%d frequency is -> %d",array[index],frequency);
   }
}
