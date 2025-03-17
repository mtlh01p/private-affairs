#include <stdio.h>
#include <math.h>
int main() {
    int a1, b1, c1, a2, b2, c2;
    float caldemx, caldemy, x, y;
    char strx[20], stry[20];
    printf("Enter the values for a1, b1, c1, a2, b2, c2:");
    scanf("%d %d %d %d %d %d", &a1, &b1, &c1, &a2, &b2, &c2);
    caldemx = (a1 * b2) - (a2 * b1);
    caldemy = (a1 * b2) - (a2 * b1);
    if (caldemx != 0 && caldemy != 0) {
        x = ((b2 * c1) - (b1 * c2)) / caldemx;
        y = ((a1 * c2) - (a2 * c1)) / caldemy;
        sprintf(strx, "%f", x);
        sprintf(stry, "%f", y);
        printf("x = %s and y = %s", strx, stry);
    }else{
        printf("Unable to compute because the denominator is zero!");
    }
    return 0;
}