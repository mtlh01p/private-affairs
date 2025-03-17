/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
int numDigits1(int num);
void numDigits2(int num, int *result);
int main()
{
    int number, result = 0;

    printf("Enter the number: \n");
    scanf("%d", &number);
    printf("numDigits1(): %d\n", numDigits1(number));
    numDigits2(number, &result);
    printf("numDigits2(): %d\n", result);
    return 0;
}
int numDigits1(int num)
{
    /*edit*/
    /* Write your code here */
    int no_of_digits = 0;
    float modif_num = num;
    while (modif_num > 1)
    {
        modif_num /= 10;
        no_of_digits++;
    }
    return (no_of_digits);
    /*end_edit*/
}
void numDigits2(int num, int *result)
{
    /*edit*/
    /* Write your code here */
    *result = numDigits1(num);
    /*end_edit*/
}