/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
int rNumDigits1(int num);
void rNumDigits2(int num, int *result);
int main()
{
    int number, result = 0;

    printf("Enter the number: \n");
    scanf("%d", &number);
    printf("rNumDigits1(): %d\n", rNumDigits1(number));
    rNumDigits2(number, &result);
    printf("rNumDigits2(): %d\n", result);
    return 0;
}
int rNumDigits1(int num)
{
    /*edit*/
    /* Write your code here */
    int no_of_dig = 0;
    while (num >= 1)
    {
        no_of_dig++;
        num /= 10;
    }
    return (no_of_dig);
    /*end_edit*/
}
void rNumDigits2(int num, int *result)
{
    /*edit*/
    /* Write your code here */
    *result = rNumDigits1(num);
    /*end_edit*/
}