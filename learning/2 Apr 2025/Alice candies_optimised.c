#include <stdio.h>

int main() {
    long N;
    scanf("%ld", &N);
    
    int no_of_sets = 0; 
    for (long k = 1; k * (k - 1) / 2 < N; k++) {
        if ((N - k * (k - 1) / 2) % k == 0) {
            no_of_sets++; 
        }
    }
    printf("%d\n", no_of_sets);
    return 0;
}