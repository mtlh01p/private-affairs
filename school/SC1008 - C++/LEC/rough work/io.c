#include <stdio.h>
#include <math.h>
#include <string.h>
float basefare = 1.5;
const float increment = 0.1;
int origin_code = 0;
int dest_code = 0;
char tel[] = "Thank you for travelling with SMRT.";
char er[] = "Please approach our Passenger Service Centre for assistance.";

int main() {
    char payway[2];
    printf("Please enter station codes of origin station and destination station. \n");
    printf("For example, 15 25: ");
    scanf("%d %d", &origin_code, &dest_code);
    if(origin_code >= 1 && dest_code >= 1) {
        float diff = 0;
        if (dest_code > origin_code) {
            diff = dest_code - origin_code;
        }else{
            diff = origin_code - dest_code;
        }
        float fare = basefare + (diff/2.0) * increment;
        if(fare > 3.10) {
            fare = 3.10;
        }
        printf("Your fare is $%.2f. Please tap your card. \n", fare);
        scanf(" %c", &payway[0]);
        payway[1] = '\0';
        if(strcmp(payway, "A") == 0) {
            printf("PASS USAGE \n%s", tel);
        }else if(strcmp(payway, "B") == 0) {
            printf("BANK CARD \n%s", tel);
        }else if(strcmp(payway, "C") == 0) {
            printf("STORED-VALUE CARD \n%s", tel);
        }else{
            printf("%s", er);
        }
    }else{
        printf("MISSED TAP.\n%s", er);
    }
    return 0;
}