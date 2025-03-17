// Online C compiler to run C program online
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    // Write C code here
    float x = 0;
    float bas = 1;
    printf("Enter x: \n");
    scanf("%f", &x);
    for(int i=1; i<=10; i++) {
        float top = pow(x, i);
        float bot = 1.0;
        for(int j=i; j>=1; j--) {
            bot *= j;
        }
        bas += (top/bot);
    }
    printf("Result = %.2f", bas);
    return 0;
}