#include <stdio.h>

int get_msb_pos(int n) {
    if (n == 0) return -1;
    int pos = 0;
    while (n > 1) {
        n >>= 1;
        pos++;
    }
    return pos;
}
long long max(long long a, long long b) {
    return (a > b) ? a : b;
}

int main() {
    int C;
    scanf("%d", &C);

    long long max_product = 0;

    if (C == 0) {
        printf("0\n");
        return 0;
    }
    int msb_pos_C = get_msb_pos(C);
    int max_val_allowed_exclusive_A_B = 1 << (msb_pos_C + 1);
    for (int A_val = 0; A_val < max_val_allowed_exclusive_A_B; A_val++) {
        int B_val = A_val ^ C;
        if (B_val < max_val_allowed_exclusive_A_B) {
            max_product = max(max_product, (long long)A_val * B_val);
        }
    }

    printf("%lld\n", max_product);

    return 0;
}
