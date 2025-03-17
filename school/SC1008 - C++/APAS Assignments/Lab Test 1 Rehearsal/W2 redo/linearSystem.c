#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    // Write C code here
    int a1, b1, c1, a2, b2, c2 = 0;
    printf("Enter the values for a1, b1, c1, a2, b2, c2: \n");
    scanf("%d %d %d %d %d %d", &a1, &b1, &c1, &a2, &b2, &c2);
    int dev = (a1 * b2) - (a2 * b1);
    if(dev != 0) {
        float x = ((b2 * c1) - (b1 * c2))/dev;
        float y = ((a1 * c2) - (a2 * c1))/dev;
        printf("x = %.2f and y = %.2f", x, y);
    }else{
        printf("Unable to compute because the denominator is zero!");
    }
    return 0;
}