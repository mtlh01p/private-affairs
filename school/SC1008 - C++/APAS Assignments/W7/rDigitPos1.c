#include <stdio.h> 
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
int rDigitPos1(int num, int digit); 
void rDigitPos2(int num, int digit, int *pos); 
int main() 
{ 
   int number, digit, result=0; 
printf("Enter the number: \n"); 
   scanf("%d", &number); 
printf("Enter the digit: \n"); 
   scanf("%d", &digit);             
printf("rDigitPos1(): %d\n", rDigitPos1(number, digit));            
   rDigitPos2(number, digit, &result);           
printf("rDigitPos2(): %d\n", result);    
return 0; 
} 

int rDigitPos1(int num, int digit)  
{ 
   char num_str[20];
   itoa(num, num_str, 10);
   if(num_str[strlen(num_str)-1] == (digit+'0')) {
    return(1);
   }else{
    return(1+rDigitPos1(num/10-(num%10/10*1), digit));
   }
} 
void rDigitPos2(int num, int digit, int *pos) 
{  
    if(pos != NULL) { 
        *pos = rDigitPos1(num, digit);
    }
} 