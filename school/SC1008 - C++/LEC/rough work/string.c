#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int main() {
    char psamsg[80], *p;
    char *close = "Thank you.";
    fgets(psamsg, 80, stdin);
    if(p = strchr(psamsg, '\n')) {
        *p = '\0';
    }
    printf("%s. %s \n", psamsg, close); 
    printf(strcat(psamsg, close));
    return 0;
}