#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int N;
    scanf("%d", &N);
    while(getchar() != '\n');  // Clear newline

    int nums[2][N];
    int count_changeables[2] = {0, 0};
    int sum[2] = {0, 0};

    for (int i = 0; i < 2; i++) {
        char input[100];
        fgets(input, sizeof(input), stdin);
        char *token = strtok(input, " ");
        int idx = 0;
        while (token != NULL) {
            nums[i][idx] = atoi(token);
            if (nums[i][idx] == -1)
                count_changeables[i]++;
            else
                sum[i] += nums[i][idx];
            idx++;
            token = strtok(NULL, " ");
        }
    }

    int total_missing = count_changeables[0] + count_changeables[1];

    if (total_missing == 1) {
        // One -1: Calculate required positive value
        int missing_row = count_changeables[0] == 1 ? 0 : 1;
        int required = sum[1 - missing_row] - sum[missing_row];
        if (required > 0)
            printf("1\n");
        else
            printf("0\n");
    } else if (count_changeables[0] == 1 && count_changeables[1] == 1) {
        // One -1 in each row — always infinite positive integer pairs that balance the sum
        printf("Infinite\n");
    } else {
        // Two -1s in one row
        int missing_row = count_changeables[0] == 2 ? 0 : 1;
        int required = sum[1 - missing_row] - sum[missing_row];
        if (required >= 2)
            printf("%d\n", required - 1);
        else
            printf("0\n");
    }

    return 0;
}
