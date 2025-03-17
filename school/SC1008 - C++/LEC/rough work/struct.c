#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>
    struct station {
        char line[3];
        int code;
        char name[50];
    };

int main() {
    // Write C code here
    char *p;
    char opp[8][3] = {"NS", "EW", "CG", "NE", "CC", "CE", "DT", "TE"};
    struct station journey[2];
    printf("Pls enter the line (NS/EW/CG/NE/CC/CE/DT/TE): ");
    fgets(journey[0].line, 3, stdin);
    if(p = strchr(journey[0].line, '\n')) {
        *p = '\0';
    }
    bool valid = false;
    for(int i=0; i<8; i++) {
        if(strcmp(journey[0].line, opp[i]) == 0) {
            valid = true;
            strcpy(journey[1].line, journey[0].line);
        }
    }
    if(valid) {
        int num_journey[2];
        printf("Pls enter the START station number: ");
        scanf(" %d", &num_journey[0]);
        printf("Pls enter the END station number: ");
        scanf(" %d", &num_journey[1]);
        if((num_journey[0] <= 40 && num_journey[0] > 0) && (num_journey[1] <= 40 && num_journey[1] > 0)) {
            for(int i=0; i<2; i++) {
                journey[i].code = num_journey[i];
            }
            while (getchar() != '\n'); 
            char *x;
            printf("Pls enter the START station name: ");
            fgets(journey[0].name, 50, stdin);
            if(x = strchr(journey[0].name,'\n')) {
                *x = '\0';
            }
            char *y;
            printf("Pls enter the END station name: ");
            fgets(journey[1].name, 50, stdin);
            if(y = strchr(journey[1].name,'\n')) {
                *y = '\0';
            }
            if((strcmp(journey[0].name, " ") != 0) && (strcmp(journey[0].name, " ") != 0)) {
                printf("Next station, %s%d %s. \nThis train service will end at %s%d %s. \nDOORS OPENING >>>", journey[0].line, journey[0].code, journey[0].name, journey[1].line, journey[1].code, journey[1].name);
            }else{
                printf("You did not enter a valid station name.");
            }
        }else{
            printf("You did not enter a valid station code.");
        }
    }else{
        printf("You did not enter a valid line code.");
    }
    return 0;
}