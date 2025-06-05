#include <stdio.h>
#include <string.h> // For memset
#include <limits.h> // For CHAR_BI

// Function to find the position of the Most Significant Bit (MSB)
// For a non-zero integer x, it returns k such that 2^k <= x < 2^(k+1)
int get_msb_pos(int n) {
    if (n == 0) return -1; // Or handle as per problem constraints for 0
    int pos = 0;
    while (n > 1) {
        n >>= 1;
        pos++;
    }
    return pos;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int N;
        scanf("%d", &N);
        
        // Max possible MSB position for a 31-bit integer is 30.
        // We need an array to store counts for each MSB position.
        // Assuming integers are positive and fit in 31 bits (up to 2*10^9)
        int msb_counts[32]; // Max bit position for an int (31 for 32-bit int)
        memset(msb_counts, 0, sizeof(msb_counts));

        for (int i = 0; i < N; i++) {
            int num;
            scanf("%d", &num);
            if (num > 0) { // Only positive numbers have a well-defined MSB for this logic
                           // If 0s are allowed, adjust logic for them or consider them having MSB at -1
                int pos = get_msb_pos(num);
                msb_counts[pos]++;
            }
        }

        long long total_pairs = (long long)N * (N - 1) / 2;
        long long invalid_pairs = 0;

        for (int i = 0; i < 32; i++) {
            if (msb_counts[i] > 1) {
                // If there are 'k' numbers with MSB at position 'i',
                // there are k * (k - 1) / 2 pairs among them.
                invalid_pairs += (long long)msb_counts[i] * (msb_counts[i] - 1) / 2;
            }
        }

        printf("%lld\n", total_pairs - invalid_pairs);
    }
    return 0;
}
