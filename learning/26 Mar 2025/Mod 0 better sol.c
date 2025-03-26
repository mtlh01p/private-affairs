#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
    int no_of_data = 0;
    scanf("%d", &no_of_data);
    while (getchar() != '\n');

    // Dynamically allocate input buffer
    char *inputted = (char *)malloc(no_of_data * sizeof(char) * 10);
    if (inputted == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    fgets(inputted, no_of_data * sizeof(char) * 10, stdin);
    char *p;
    if ((p = strchr(inputted, '\n'))) {
        *p = '\0';
    }

    // Dynamically allocate list_of_nums
    int *list_of_nums = (int *)malloc(no_of_data * sizeof(int));
    if (list_of_nums == NULL) {
        printf("Memory allocation failed.\n");
        free(inputted);
        return 1;
    }

    int indexing = 0;
    int pos = 0;
    int prev = 0;

    while (inputted[pos] != '\0') {
        if (inputted[pos] == ' ' || inputted[pos] == '\0') {
            char temp[pos - prev + 1];
            int pos2 = 0;
            for (int i = prev; i < pos; i++) {
                temp[pos2++] = inputted[i];
            }
            temp[pos - prev] = '\0';
            list_of_nums[indexing++] = atoi(temp) % 10;
            prev = pos + 1;
        }
        pos++;
    }

    // Add logic to process the last number
    if (prev < pos) {
        char temp[pos - prev + 1];
        int pos2 = 0;
        for (int i = prev; i < pos; i++) {
            temp[pos2++] = inputted[i];
        }
        temp[pos - prev] = '\0';
        list_of_nums[indexing++] = atoi(temp) % 10;
    }

    int num_to_eval = 0;
    int power_of_ten = 1;

    for (int i = 0; i < no_of_data - 1; i++) {
        power_of_ten *= 10;  // Precompute power of ten
    }

    for (int i = 0; i < no_of_data; i++) {
        num_to_eval += list_of_nums[i] * power_of_ten;
        power_of_ten /= 10; // Reduce power iteratively
    }

    if (num_to_eval % 10 == 0) {
        printf("Yes");
    } else {
        printf("No");
    }

    // Free allocated memory
    free(inputted);
    free(list_of_nums);

    return 0;
}