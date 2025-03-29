#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

bool *buildSieve(int max) {
    bool *sieve = (bool *)malloc((max + 1) * sizeof(bool));
    for (int i = 0; i <= max; i++) sieve[i] = true;
    sieve[0] = sieve[1] = false;

    for (int i = 2; i * i <= max; i++) {
        if (sieve[i]) {
            for (int j = i * i; j <= max; j += i) sieve[j] = false;
        }
    }
    return sieve;
}

int countPrimeTriplets(int *arr, int N, bool *sieve, int sieveSize) {
    int triplets = 0;
    for (int a = 0; a < N - 2; a++) {
        for (int b = a + 1; b < N - 1; b++) {
            for (int c = b + 1; c < N; c++) {
                long long product = (long long)arr[a] * arr[b] * arr[c];
                if (product <= sieveSize && sieve[product]) {
                    triplets++;
                }
            }
        }
    }
    return triplets;
}

int main() {
    int num;
    scanf("%d", &num);

    for (int t = 0; t < num; t++) {
        int N;
        scanf("%d", &N);

        int *list_of_nums = (int *)malloc(N * sizeof(int));
        int maxNum = 0;

        for (int i = 0; i < N; i++) {
            scanf("%d", &list_of_nums[i]);
            if (list_of_nums[i] > maxNum) maxNum = list_of_nums[i];
        }
        int sieveLimit = maxNum * maxNum * maxNum;
        bool *sieve = buildSieve(sieveLimit);

        int triplets = countPrimeTriplets(list_of_nums, N, sieve, sieveLimit);

        printf("%d\n", triplets);

        free(list_of_nums);
        free(sieve);
    }
    return 0;
}