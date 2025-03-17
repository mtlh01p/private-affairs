/*edit*/

/*custom header*/
#include <string.h>
/*end_edit*/
#include <stdio.h>
int rDigitPos1(int num, int digit);
void rDigitPos2(int num, int digit, int *pos);
int main()
{
    int number, digit, result = 0;

    printf("Enter the number: \n");
    scanf("%d", &number);
    printf("Enter the digit: \n");
    scanf("%d", &digit);
    printf("rDigitPos1(): %d\n", rDigitPos1(number, digit));
    rDigitPos2(number, digit, &result);
    printf("rDigitPos2(): %d\n", result);
    return 0;
}
int rDigitPos1(int num, int digit)
{
    /*edit*/
    /* Write your code here */
    int no_of_dig = 0;
    int num2 = num;
    while (num2 >= 1)
    {
        no_of_dig++;
        num2 /= 10;
    }
    char num_str[no_of_dig + 1];
    sprintf(num_str, "%d", num);
    char digit_str[2];
    sprintf(digit_str, "%d", digit);
    int i = 0;
    for (i = 1; i <= no_of_dig; i++)
    {
        if (num_str[no_of_dig - i] == digit_str[0])
        {
            return (i);
            break;
        }
    }
    return (0);
    /*end_edit*/
}
void rDigitPos2(int num, int digit, int *pos)
{
    /*edit*/
    /* Write your code here */
    *pos = rDigitPos1(num, digit);
    /*end_edit*/
}