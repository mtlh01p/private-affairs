#include <stdio.h>
#include <string.h>
#include <math.h>

int main() {
    char lines[6][40] = {"North-South Line", "East-West Line", "North East Line", "Circle Line", "Downtown Line", "Thomson-East Coast Line"};
    char op[6][5] = {"SMRT", "SMRT", "SBST", "SMRT", "SBST", "SMRT"};
    printf("Lines operated by SMRT: \n");
    int n = 0;
    for(int i=0; i<6; i++) {
        if(strcmp(op[i], "SMRT") == 0) {
            printf("%d. %s \n", ++n, lines[i]);
        }
    }
    n = 0;
    printf("Lines operated by SBS Transit: \n");
    for(int i=0; i<6; i++) {
        if(strcmp(op[i], "SBST") == 0) {
            printf("%d. %s \n", ++n, lines[i]);
        }
    }
    return 0;
}