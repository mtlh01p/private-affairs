#include <stdio.h>
#include <stdlib.h>

#define MAX 1000001

int spf[MAX];

void computeSPF() {
    for (int i = 2; i < MAX; i++) {
        if (spf[i] == 0) {
            for (int j = i; j < MAX; j += i) {
                if (spf[j] == 0) spf[j] = i;
            }
        }
    }
}

int main() {
    computeSPF();
    
    int T;
    scanf("%d", &T);
    
    while (T--) {
        int X;
        scanf("%d", &X);

        if (X == 2) {
            printf("500000\n");
            continue;
        }

        int count = 0;
        for (int i = 2; i < MAX; i++) {
            if (spf[i] == X) {
                count++;
            }
        }

        printf("%d\n", count);
    }

    return 0;
}
