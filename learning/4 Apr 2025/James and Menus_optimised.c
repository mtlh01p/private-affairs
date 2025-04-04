#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_N 1000
#define MAX_M 1000

int pricings[MAX_N][MAX_M];
int bests[MAX_N];

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    char inputted[12000];
    for (int i = 0; i < n; i++) {
        bests[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        scanf(" %[^\n]", inputted);
        char *token = strtok(inputted, " ");
        int j = 0;
        while (token != NULL) {
            pricings[i][j] = atoi(token);
            token = strtok(NULL, " ");
            j++;
        }
    }
    for (int j = 0; j < m; j++) {
        int max_price = 0;

        // Find max price for item j
        for (int i = 0; i < n; i++) {
            if (pricings[i][j] > max_price) {
                max_price = pricings[i][j];
            }
        }

        // Step 2: Count how many times each menu has a max price
        for (int i = 0; i < n; i++) {
            if (pricings[i][j] == max_price) {
                bests[i]++;
            }
        }
    }

    // Step 3: Find the menu with the highest count of "good" prices
    int max_count = 0, best_menu = -1;
    for (int i = 0; i < n; i++) {
        if (bests[i] > max_count) {
            max_count = bests[i];
            best_menu = i;
        }
    }

    // Step 4: If multiple menus have the same max count, find the one with the highest average price
    double max_avg = 0.0;
    for (int i = 0; i < n; i++) {
        if (bests[i] == max_count) {
            double sum = 0;
            for (int j = 0; j < m; j++) {
                sum += pricings[i][j];
            }
            double avg = sum / m;
            if (avg > max_avg) {
                max_avg = avg;
                best_menu = i;
            }
        }
    }

    printf("%d\n", best_menu + 1);  // Convert 0-based index to 1-based
    return 0;
}