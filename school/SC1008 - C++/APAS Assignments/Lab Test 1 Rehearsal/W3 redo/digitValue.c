// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int digitValue1(int num, int k);
void digitValue2(int num, int k, int *result);

int main() {
    // Write C code here
     int num, digit, result=-1; 
     printf("Enter the number: \n"); 
     scanf("%d", &num);      
     printf("Enter k position: \n"); 
     scanf("%d", &digit);    
     printf("digitValue1(): %d\n",  digitValue1(num, digit)); 
     digitValue2(num, digit, &result); 
     printf("digitValue2(): %d\n", result);    
     return 0;
}
int digitValue1(int num, int k) {
    char num_str[20];
    sprintf(num_str, "%d", num);
    if(k >= 1 && k <= strlen(num_str)) {
        char n = num_str[strlen(num_str)-k];
        return(n - '0');
    }else{
        return(0);
    }
}
void digitValue2(int num, int k, int *result) {
    *result = digitValue1(num, k);
}