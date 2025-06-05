#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        unsigned long long N;
        scanf("%llu", &N);
    
        int count = 0;
        unsigned long long temp = N;
        while (temp) {
            count += temp & 1;
            temp >>= 1;
        }
        printf("%d\n", count >= 2 ? 1 : 0);
    }
    return 0;
}
