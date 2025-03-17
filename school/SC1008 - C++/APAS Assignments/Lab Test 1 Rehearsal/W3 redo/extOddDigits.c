#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define INIT_VALUE 999
int extOddDigits1(int num);
void extOddDigits2(int num, int *result);

int main () {
    int number, result = INIT_VALUE; 
    printf("Enter a number: \n"); 
    scanf("%d", &number); 
    printf("extOddDigits1(): %d\n", extOddDigits1(number));         
    extOddDigits2(number, &result); 
    printf("extOddDigits2(): %d\n", result); 
    return 0;
}

int extOddDigits1(int num) {
    int length = 0;
    int num2 = num;
    while(num2 > 1) {
        num2 /= 10;
        length += 1;
    }
    char num_str[length];
    char num_str2[20];
    itoa(num, num_str, 10);
    int indexer = 0;
    for(int i=0; i<length; i++) {
        if((num_str[i] - '0') % 2 != 0) {
            num_str2[indexer] = num_str[i];
            indexer += 1;
        }
    }
    num_str2[length] == '\0';
    int to_ret = atoi(num_str2);
    return(to_ret);
}

void extOddDigits2 (int num, int *result) {
    *result = extOddDigits1(num);
}