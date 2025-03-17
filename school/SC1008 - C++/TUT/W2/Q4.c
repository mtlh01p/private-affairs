#include <stdio.h>
#include <math.h>
int main() {
    int i, j;
    float mult, x;
    float res = 1.0;
    float div;
    printf("Enter x: \n");
    scanf("%f", &x);
    for(i=1; i<=10; i++) {
        mult = pow(x, i);
        div = 1;
        for(j=1; j<=i; j++) {
            div *= j;
        }
        res += (mult/div);
    }
    printf("Result: %f \n", res);
    return 0;
}