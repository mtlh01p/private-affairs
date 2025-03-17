/*edit*/

/*custom header*/
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
/*end_edit*/
#include <stdio.h>
int main()
{
    /*edit*/
    /* Write your code here */
    int lin, i, summ, num, num_en;
    char entered[1000];

    printf("Enter number of lines: \n");
    scanf("%d", &lin);
    getchar();

    for (i = 0; i < lin; i++)
    {
        num = 0;
        summ = 0;
        num_en = 0;
        printf("Enter line %d (end with -1): \n", i + 1);
        fgets(entered, sizeof(entered), stdin);

        char *pos;
        if ((pos = strchr(entered, '\n')) != NULL)
        {
            *pos = '\0';
        }

        char *token = strtok(entered, " ");
        while (token != NULL)
        {
            num_en = atoi(token);
            if (num_en == -1)
            {
                break;
            }
            summ += num_en;
            num++;
            token = strtok(NULL, " ");
        }
        if (num > 0)
        {
            printf("Average = %.2f \n", (float)summ / num);
        }
        else
        {
            printf("No numbers were entered\n");
        }
    }

    /*end_edit*/

    return 0;
}