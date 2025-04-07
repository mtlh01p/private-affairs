#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;

    while (exp > 0) {
        if (exp % 2 == 1)
            result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }

    return result;
}

int GCD(int *Num, int size) {
    int possibles[1000];
    int possibles_f = 0;
    for(int i = 2; i <= Num[0]; i++) {
        if(Num[0] % i == 0) {
            int validity = 1;
            for(int j = 1; j < size; j++) {
                if(Num[j] % i != 0) {
                    validity = 0;
                    break;
                }
            }
            if(validity) {
                possibles[possibles_f++] = i;
            }
        }
    }
    return possibles[possibles_f - 1];
}

int main() {
    int N;
    scanf("%d", &N);
    int nums[N];
    int nums_c = 0;
    long long fx = 1;
    char inputted[250], *p;
    while (getchar() != '\n');
    fgets(inputted, 250, stdin);
    if ((p = strchr(inputted, '\n'))) {
        *p = '\0';
    }
    char *token = strtok(inputted, " ");
    while (token != NULL) {
        nums[nums_c++] = atoi(token);
        fx = (fx * nums[nums_c - 1]) % 1000000007;
        token = strtok(NULL, " ");
    }
    int gx = GCD(nums, nums_c);
    long long val = mod_pow(fx, gx, 1000000007);
    printf("%lld\n", val); 
    return 0;
}
