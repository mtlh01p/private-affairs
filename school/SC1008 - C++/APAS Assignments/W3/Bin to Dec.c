/*edit*/

/*custom header*/
#include <string.h>
/*end_edit*/
#include <stdio.h>
#include <math.h>
int main()
{
    /*edit*/
    /* Write your code here */
    int i, panjang, result = 0;
    char stringbin[1000];
    printf("Enter a binary number: \n");
    scanf("%s", &stringbin);
    panjang = strlen(stringbin);
    for (i = 0; i < panjang; i++)
    {
        int val = stringbin[panjang - 1 - i] - '0';
        result += (val *= pow(2, i));
    }
    printf("The equivalent decimal number: %d", result);
    /*end_edit*/
    return 0;
}