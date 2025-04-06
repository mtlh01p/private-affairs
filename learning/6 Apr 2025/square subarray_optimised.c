#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
    int N;
    scanf("%d", &N);
    int nums[N];
    int nums_c = 0;
    char inputted[40010], *p;
    while (getchar() != '\n');
    fgets(inputted, 40010, stdin);
    if ((p = strchr(inputted, '\n'))) {
        *p = '\0';
    }
    char *token = strtok(inputted, " ");
    while (token != NULL) {
        nums[nums_c++] = atoi(token);
        token = strtok(NULL, " ");
    }
    int prefix_sum[N + 1];
    prefix_sum[0] = 0;
    for (int i = 0; i < N; i++) {
        prefix_sum[i + 1] = prefix_sum[i] + nums[i];
    }
    int good = 0;
    for (int i = 0; i < N; i++) {
        for (int end = i; end < N; end++) {
            int sums = prefix_sum[end + 1] - prefix_sum[i];
            int root = (int)sqrt(sums);
            if (root * root == sums) {
                good++;
            }
        }
    }
    printf("%d", good);
    return 0;
}