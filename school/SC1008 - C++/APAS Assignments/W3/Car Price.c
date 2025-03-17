/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
int main()
{
    /*edit*/
    /* Write your code here */
    int list_price, category;
    float discounted_price, gst, lxt = 0, coe = 0;
    printf("Please enter the list price: \n");
    scanf("%d", &list_price);
    printf("Please enter the category: \n");
    scanf("%d", &category);
    discounted_price = 0.9 * list_price;
    gst = 0.03 * discounted_price;
    if (discounted_price > 100000)
    {
        lxt = 0.1 * discounted_price;
    }
    switch (category)
    {
    case 1:
        coe = 70000;
        break;
    case 2:
        coe = 80000;
        break;
    case 3:
        coe = 23000;
        break;
    case 4:
        coe = 600;
        break;
    }
    printf("Total price is $%.2f", (discounted_price + gst + lxt + coe));
    /*end_edit*/
    return 0;
}