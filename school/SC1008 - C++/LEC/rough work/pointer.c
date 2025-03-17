#include <stdio.h>
#include <math.h>

int main() {
    float base_fare = 1.5;
    int *address;
    int a;
    printf("Minimum travel fare = %.1f. Data stored at address %p. \n Please enter your ID: \n", base_fare, &base_fare);
    scanf(" %d", &a);
    address = &a;
    printf("You entered number %d.", *address);
    return 0;
}