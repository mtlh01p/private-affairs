#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
    int table[4][2];
    for(int i=0; i<4; i++) {
        printf("Pls enter the values for row %d: \n", i+1);
        for(int j=0; j<2; j++) {
            printf("Pls enter the value for column %d: ", j+1);
            scanf(" %d", &table[i][j]);
        }
    }
    printf("The result is this thing: \n");
    for(int i=0; i<4; i++) {
        for(int j=0; j<2; j++) {
            printf("| %d |", *(*(table+i) + j));
        }
        printf("\n");
    }
    return 0;
}