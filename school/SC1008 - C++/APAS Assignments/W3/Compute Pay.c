/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
double computePay1(int noOfHours, int payRate);
void computePay2(int noOfHours, int payRate, double *grossPay);
int main()
{
    int noOfHours, payRate;
    double grossPay;

    printf("Enter number of hours: \n");
    scanf("%d", &noOfHours);
    printf("Enter hourly pay rate: \n");
    scanf("%d", &payRate);
    printf("computePay1(): %.2f\n", computePay1(noOfHours, payRate));
    computePay2(noOfHours, payRate, &grossPay);
    printf("computePay2(): %.2f\n", grossPay);
    return 0;
}
double computePay1(int noOfHours, int payRate)
{
    /*edit*/
    /* Write your code here */
    int paycheck = 0;
    if (noOfHours <= 160)
    {
        paycheck = noOfHours * payRate;
    }
    else
    {
        paycheck = 160 * payRate + ((noOfHours - 160) * payRate * 1.5);
    }
    return (paycheck);
    /*end_edit*/
}
void computePay2(int noOfHours, int payRate, double *grossPay)
{
    /*edit*/
    /* Write your code here */
    *grossPay = computePay1(noOfHours, payRate);
    /*end_edit*/
}