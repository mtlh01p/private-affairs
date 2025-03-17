#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    // Write C code here
    int digits, letters = 0;
    char entered[50], *p;
    printf("Enter your characters (# to end): \n");
    fgets(entered, 50, stdin);
    if(p = strchr(entered, '\n')) {
        *p = '\0';
    }
    int i = 0;
    while(entered[i] != '#') {
        if(isalpha(entered[i])) {
            letters += 1;
        }else if(isdigit(entered[i])){
            digits += 1;
        }
        i++;
    }
    printf("The number of digits: %d \n", digits);
    printf("The number of letters: %d \n", letters);
    return 0;
}