#include <stdio.h>

int main() {
    long N;
    scanf("%ld", &N);
    int no_of_sets = 0; 
    long k = 1;
    while (k <= N) {
        long tempo_sum = 0;
        long k_temp = k;
        while (tempo_sum < N) {
            tempo_sum += k_temp;
            k_temp += 2;
        }
        if (tempo_sum == N) {
            no_of_sets++;
        }
        k += 2; 
    }

    printf("%d\n", no_of_sets); 
    return 0;
}