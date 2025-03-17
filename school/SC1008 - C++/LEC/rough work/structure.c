#include <stdio.h>
#include <math.h>
float basefare = 2.5;
const float increment = 0.1;

int main() {
    for(int i=0; i<10; i++) {
        double x = basefare + (i+1) * increment;
        printf("Hello world %.1f \n", x);
    }
    return 0;
}