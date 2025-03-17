#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    // Write C code here
    printf("Pls enter number sample here: ");
    char pay[80], *p;
    fgets(pay, 80, stdin);
    if(p=strchr(pay, '\n')) {
        *p = '\0';
    }
    bool Num = true;
    for(int i=0; i<strlen(pay); i++) {
        if(!isdigit(pay[i])) {
            Num = false;
            break;
        }
    }
    if(Num) {
        int k = atoi(pay);
        printf("Your number added by 10 is %d.", (k+10));
    }else{
        printf("You didn't enter a number do you?");
    }
}