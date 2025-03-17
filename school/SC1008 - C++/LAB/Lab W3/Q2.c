/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
int square1(int num);
void square2(int num, int *result);
int main()
{
    int number, result = 0;

    printf("Enter the number: \n");
    scanf("%d", &number);
    printf("square1(): %d\n", square1(number));
    square2(number, &result);
    printf("square2(): %d\n", result);
    return 0;
}
int square1(int num)
{
    /*edit*/
    /* Write your code here */
    int k;
    k = num * num;
    return (k);
    /*end_edit*/
}
void square2(int num, int *result)
{
    /*edit*/
    /* Write your code here */
    *result = square1(num);
    /*end_edit*/
}