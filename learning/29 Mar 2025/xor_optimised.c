#include <stdio.h>

long xorToN(long n) {
    if (n % 4 == 0) return n;
    if (n % 4 == 1) return 1;
    if (n % 4 == 2) return n + 1;
    return 0;
}

int main() {
    long L, R;
    scanf("%ld %ld", &L, &R);

    long xorResult = xorToN(R) ^ xorToN(L - 1);
    
    if (xorResult % 2 == 0) {
        printf("even\n");
    } else {
        printf("odd\n");
    }

    return 0;
}