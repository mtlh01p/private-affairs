// Online C compiler to run C program online
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    // Write C code here
    int height = 0;
    printf("Enter the height: \n");
    scanf("%d", &height);
    printf("Pattern: \n");
    for(int i=0; i<height; i++) {
        if(i%3 == 0) {
            for(int j=0; j<=i; j++) {
                printf("%d", 1);
            }
        }else if(i%3 == 1) {
            for(int j=0; j<=i; j++) {
                printf("%d", 2);
            }
        }else{
            for(int j=0; j<=i; j++) {
                printf("%d", 3);
            }
        }
        printf("\n");
    }
    return 0;
}