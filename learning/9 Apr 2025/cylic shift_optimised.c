#include <stdio.h>
#include <string.h>

void left_shift(char *s, int n) {
    char first = s[0];
    for (int i = 0; i < n - 1; i++) {
        s[i] = s[i + 1];
    }
    s[n - 1] = first;
}

int find_cycle_length(char *s, int n) {
    char temp[n + 1];
    strcpy(temp, s);
    int count = 0;
    do {
        left_shift(temp, n);
        count++;
    } while (strcmp(temp, s) != 0);
    return count;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int N;
        long long K;
        scanf("%d %lld", &N, &K);
        char s[N + 1];
        scanf("%s", s);
        left_shift(s, N);
        int cycle_len = find_cycle_length(s, N);
        long long result = (long long)cycle_len * K;
        printf("%lld\n", (result-1));
    }
    return 0;
}

