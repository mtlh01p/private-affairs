#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int num;
    scanf(" %d", &num);
    int a_nums[num];
    int a_nums_pos = 0;
    int b_nums[num];
    int b_nums_pos = 0;

    while (getchar() != '\n');

    char a[50], *p;
    char b[50], *q;

    fgets(a, 50, stdin);
    while ((p = strchr(a, '\n'))) {
        *p = '\0';
    }
    fgets(b, 50, stdin);
    while ((q = strchr(b, '\n'))) {
        *q = '\0';
    }

    int pos = 0;
    for (int i = 0; i <= strlen(a); i++) {
        if (a[i] == ' ' || a[i] == '\0') {
            char eval[20] = {0};
            int pos2 = 0;
            for (int j = pos; j < i; j++) {
                eval[pos2++] = a[j];
            }
            eval[pos2] = '\0';
            a_nums[a_nums_pos++] = atoi(eval);
            pos = i + 1;
        }
    }

    pos = 0;
    for (int i = 0; i <= strlen(b); i++) {
        if (b[i] == ' ' || b[i] == '\0') {
            char eval[20] = {0};
            int pos2 = 0;
            for (int j = pos; j < i; j++) {
                eval[pos2++] = b[j];
            }
            eval[pos2] = '\0';
            b_nums[b_nums_pos++] = atoi(eval);
            pos = i + 1;
        }
    }

    int combs[num][100];
    for (int i = 0; i < num; i++) {
        for (int j = 0; j < 100; j++) {
            combs[i][j] = 10000; 
        }
    }
    for (int i = 0; i < num; i++) {
        int indexing = 1;
        int to_red = a_nums[i];
        combs[i][0] = to_red;
        while (to_red >= b_nums[i]) {
            combs[i][indexing++] = to_red - b_nums[i];
            to_red -= b_nums[i];
        }
    }

    int search[100];
    for (int i = 0; i < 100; i++) {
        search[i] = combs[0][i];
    }

    int pos_check = 0;
    int value_found = 10000;
    while (search[pos_check] <= 5000 && search[pos_check] != 10000) {
        int found[num];
        found[0] = search[pos_check];
        for (int i = 1; i < num; i++) {
            found[i] = 10000;
        }
        for (int i = 1; i < num; i++) {
            int pos_check2 = 0;
            while (combs[i][pos_check2] <= 5000 && combs[i][pos_check2] != 10000) {
                if (combs[i][pos_check2] == search[pos_check]) {
                    found[i] = search[pos_check];
                    break;
                } else {
                    pos_check2++;
                }
            }
        }

        int checkpoint = 1;
        for (int j = 1; j < num; j++) {
            if (found[j] == found[0]) {
                checkpoint++;
            }
        }

        if (checkpoint == num) {
            value_found = found[0];
            break;
        }
        pos_check++;
    }

    if (value_found != 10000) {
        int steps = 0;
        for (int i = 0; i < num; i++) {
            while (a_nums[i] != value_found) {
                a_nums[i] -= b_nums[i];
                steps++;
            }
        }
        printf("%d", steps);
    } else {
        printf("-1");
    }

    return 0;
}