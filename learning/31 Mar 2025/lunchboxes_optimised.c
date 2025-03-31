#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n, m;
        scanf("%d %d", &n, &m);
        int a[m];
        for (int i = 0; i < m; i++) {
            scanf("%d", &a[i]);
        }
        qsort(a, m, sizeof(int), compare); // Sort the orders
        int schoolsServed = 0;
        int currentOrder = 0;
        for (int i = 0; i < m; i++) {
            if (currentOrder + a[i] <= n) {
                currentOrder += a[i];
                schoolsServed++;
            } else {
                break; // Stop if adding the next order exceeds n
            }
        }
        printf("%d\n", schoolsServed);
    }
    return 0;
}