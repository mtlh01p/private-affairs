#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int pricings[n][m];
    int bests[n];
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
        for (int i = 0; i < n; i++) {
            if (pricings[i][j] > max_price) {
                max_price = pricings[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            if (pricings[i][j] == max_price) {
                bests[i]++;
            }
        }
    }
    int selected[n];
    int selected_score[n];
    int selected_track = 0;
    for (int i = 0; i < n; i++) {
        selected[i] = -1;
        selected_score[i] = -1;
    }
    for (int i = 0; i < n; i++) {
        if (bests[i] > selected_score[0]) {
            for (int a = 0; a < n; a++) {
                selected[a] = -1;
                selected_score[a] = -1;
            }
            selected_score[0] = bests[i];
            selected[0] = i;
            selected_track = 0;
        } else if (bests[i] == selected_score[0]) {
            selected_track += 1;
            selected_score[selected_track] = bests[i];
            selected[selected_track] = i;
        }
    }
    if (selected[1] == -1) {
        printf("%d\n", selected[0] + 1);
    } else {
        float selected_avg[n];
        for (int i = 0; i <= selected_track; i++) {
            float total = 0;
            for (int j = 0; j < m; j++) {
                total += pricings[selected[i]][j];
            }
            selected_avg[i] = total / m;
        }
        float max_avg = 0;
        int correct = 0;
        for (int i = 0; i <= selected_track; i++) {
            if (selected_avg[i] > max_avg) {
                max_avg = selected_avg[i];
                correct = selected[i];
            }
        }

        printf("%d\n", correct + 1);
    }
    return 0;
}
