#include <stdio.h>
#include <ctype.h>
int main() {
    char c, stralphacount[3], strnumcount[3];
    int alphacount = 0;
    int numcount = 0;
    printf("Enter your characters (# to end): \n");
    while ((c = getchar()) != '#') {
        if (isalpha(c)) {
            alphacount += 1;
        }else if (isdigit(c)){
            numcount += 1;
        }
    }
    sprintf(stralphacount, "%d", alphacount);
    sprintf(strnumcount, "%d", numcount);
    printf("The number of digits: %s \n", strnumcount);
    printf("The number of letters: %s \n", stralphacount);
    return 0;
}