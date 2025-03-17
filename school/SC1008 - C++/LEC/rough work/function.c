#include <stdio.h>
#include <math.h>
#include <string.h>

char* psa(int code) {
    static char msg[200] = "Template";
    switch(code) {
        default:
        strcpy(msg, "Please do not eat or drink on the railway premises. Thank you for your cooperation.");
        break;
        case 1:
        strcpy(msg, "For passengers travelling with young children or the elderly, please use the lift. Thank you.");
        break;
        case 2:
        strcpy(msg, "Please do not block the escalators. Thank you.");
        break;
        case 3:
        strcpy(msg, "Please do not board when the lights are flashing. Thank you.");
        break;
        case 4:
        strcpy(msg, "Please do not leave your belongings unattended. If you see any suspicious looking person or article, please inform our staff or call 999.");
        break;
    }
    return msg;
}

int main() {
    int pscode = 0;
    printf("ENTER PSA CODE: ");
    scanf(" %d", &pscode);
    char *returnedmsg = psa(pscode);
    printf("%s", returnedmsg);
    return 0;
}