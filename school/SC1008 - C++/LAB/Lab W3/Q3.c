/*edit*/

/*custom header*/
#include <string.h>
/*end_edit*/
#include <stdio.h>
int digitPos1(int num, int digit);
void digitPos2(int num, int digit, int *result);
int main()
{
    int number, digit, result = 0;

    printf("Enter the number: \n");
    scanf("%d", &number);
    printf("Enter the digit: \n");
    scanf("%d", &digit);
    printf("digitPos1(): %d\n", digitPos1(number, digit));
    digitPos2(number, digit, &result);
    printf("digitPos2(): %d\n", result);
    return 0;
}
int digitPos1(int num, int digit)
{
    /*edit*/
    /* Write your code here */
    char stringnum[1000];
    char digitfind = digit + '0';
    sprintf(stringnum, "%d", num);
    int pos = 0;
    int i = 0;
    int panjang = strlen(stringnum);
    for (i = 0; i < panjang; i++)
    {
        if (pos == 0)
        {
            if (stringnum[panjang - 1 - i] == digitfind)
            {
                pos = i + 1;
            }
        }
    }
    return (pos);
    /*end_edit*/
}
void digitPos2(int num, int digit, int *result)
{
    /*edit*/
    /* Write your code here */
    *result = digitPos1(num, digit);
    /*end_edit*/
}