#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T); 
    for (int i = 0; i < T; i++) {
        long long num;
        scanf("%lld", &num);
        if (num == 1) {
            printf("YES\n"); 
        } else {
            printf("NO\n");
        }
    }
    return 0;
}