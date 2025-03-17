#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

int main() {
    char op[5];
    int op2;
    char elevated[2];
    char branching[2];
    char loong[2];
    printf("Please enter the 4-alphabet initial of the operator: ");
    scanf("%s", &op[0]);
    op[4] = '\0';
    if(strcmp(op, "SMRT") == 0) {
        op2 = 4;
    }else if (strcmp(op, "SBST") == 0){
        op2 = 2;
    }else{
        op2 = 0;
    }
    switch(op2) {
        case 4:
        printf("Is it partially elevated? (Y/N) ");
        scanf(" %c", &elevated[0]);
        elevated[1] = '\0';
        if(strcmp(elevated, "Y") == 0) {
            printf("Does it have a branch? (Y/N) ");
            scanf(" %c", &branching[0]);
            branching[1] = '\0';
            printf((strcmp(branching, "Y") == 0)? "East-West Line":"North-South Line");
        }else{
            printf("Is it long, like over 35km-long? (Y/N) ");
            scanf(" %c", &loong[0]);
            loong[1] = '\0';
            printf((strcmp(loong, "Y") == 0)? "Thomson-East Coast Line":"Circle Line");
        }
        break;
        case 2:
        printf("Is it long, like over 35km-long? (Y/N) ");
        scanf(" %c", &loong[0]);
        loong[1] = '\0';
        printf((strcmp(loong, "Y") == 0)? "Downtown Line" : "North East Line");
        break;
        default:
        printf("Jurong Region Line, maybe :P");
        break;
    }
    return 0;
}