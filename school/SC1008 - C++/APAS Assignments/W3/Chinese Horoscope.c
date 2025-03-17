/*edit*/

/*custom header*/
#include <stdbool.h>
/*end_edit*/
#include <stdio.h>
int main()
{
    /*edit*/
    /* Write your code here */
    bool Cont = true;
    while (Cont)
    {
        int year, denom;
        printf("Enter your birth year: \n");
        scanf("%d", &year);
        if (year != -1)
        {
            denom = year % 12;
            char sign[10];
            switch (denom)
            {
            case 4:
                strcpy(sign, "Rat");
                break;
            case 5:
                strcpy(sign, "Cow");
                break;
            case 6:
                strcpy(sign, "Tiger");
                break;
            case 7:
                strcpy(sign, "Rabbit");
                break;
            case 8:
                strcpy(sign, "Dragon");
                break;
            case 9:
                strcpy(sign, "Snake");
                break;
            case 10:
                strcpy(sign, "Horse");
                break;
            case 11:
                strcpy(sign, "Goat");
                break;
            case 0:
                strcpy(sign, "Monkey");
                break;
            case 1:
                strcpy(sign, "Rooster");
                break;
            case 2:
                strcpy(sign, "Dog");
                break;
            case 3:
                strcpy(sign, "Pig");
                break;
            }
            printf("chineseHoroscope: %s \n", sign);
        }
        else
        {
            Cont = false;
        }
    }
    /*end_edit*/
    return 0;
}