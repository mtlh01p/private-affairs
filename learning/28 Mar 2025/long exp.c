#include <stdio.h>

long long mod_exp(long long base, long long exp, long long mod) {
    long long result = 1;
    base = base % mod;

    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        exp = exp >> 1;
        base = (base * base) % mod;
    }

    return result;
}

int main() {
    long long bil1 = 0;
    long long bil2 = 0;
    long long modu = 1000000007;
    scanf("%lld %lld", &bil1, &bil2);
    printf("%lld\n", mod_exp(bil1, bil2, modu));
    return 0;
}
