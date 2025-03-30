#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void generateCombinations(char *input, long k, long start, char *current, long index, char **result, long *count) {
    if (index == k) {
        current[index] = '\0';
        result[*count] = strdup(current);
        (*count)++;
        return;
    }

    for (long i = start; i < strlen(input); i++) {
        current[index] = input[i];
        generateCombinations(input, k, i + 1, current, index + 1, result, count);
    }
}

char **generateAllCombinations(char *input, long k, long *resultSize) {
    long n = strlen(input);
    long maxCombinations = 1;
    for (long i = 0; i < k; i++) maxCombinations *= n - i;
    maxCombinations /= k;

    char **result = (char **)malloc(maxCombinations * sizeof(char *));
    char *current = (char *)malloc((k + 1) * sizeof(char)); 
    *resultSize = 0;

    generateCombinations(input, k, 0, current, 0, result, resultSize);

    free(current);
    return result;
}

long main(){
	long K;
	char N[20];
    long end = 0;
	char inputted[22], *p;
	fgets(inputted, 22, stdin);
	if(p=strchr(inputted, '\n')) {
		*p = '\0';
	}
	for(long i=0; i<strlen(inputted); i++) {
		if(inputted[i] == ' ') {
			for(long j=0; j<i; j++) {
				N[j] = inputted[j];
			}
			N[i] = '\0';
            end = i;
            break;
		}
	}
	K = inputted[end+1] - '0';
    long resultSize = 0;
    long digits_avail = strlen(inputted)-2;
    char **combinations = generateAllCombinations(N, digits_avail-K, &resultSize);
    long max = 0;
    for (long i = 0; i < resultSize; i++) {
        long testing = atoll(combinations[i]);
        if(testing > max) {
            max = testing;
        }
    }
	printf("%lld", max);
}