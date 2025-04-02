#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h> 

int isprime(int num) {
    if (num <= 1) {
        return 0;
    }
    if (num == 2) {
        return 1;
    }
    if (num % 2 == 0) {
        return 0;
    }
    for (int i = 3; i <= sqrt(num); i += 2) {
        if (num % i == 0) {
            return 0; //
        }
    }
    return 1; 
}

int main() {
    int num;
    scanf("%d", &num);
    while (getchar() != '\n'); 
    char *inputted = (char *)malloc(8000010 * sizeof(char));
    if (inputted == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    fgets(inputted, 8000010, stdin);
    char *token = strtok(inputted, " "); 

    int min = INT_MAX; 
    int max = INT_MIN; 

    while (token != NULL) {
        int num = atoi(token);
        if (isprime(num)) {
            if (num < min) {
                min = num; 
            }
            if (num > max) {
                max = num; 
            }
        }
        token = strtok(NULL, " ");
    }
    if (min == INT_MAX || max == INT_MIN) {
        printf("-1");
    } else {
        printf("%d", max - min);
    }
    free(inputted); 
    return 0;
}