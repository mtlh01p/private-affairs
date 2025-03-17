/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
int rAge(int studRank);
int main()
{
    int studRank;

    printf("Enter student rank: \n");
    scanf("%d", &studRank);
    printf("rAge(): %d\n", rAge(studRank));
    return 0;
}
int rAge(int studRank)
{
    /*edit*/
    /* Write your code here */
    if (studRank == 1)
    {
        return (10);
    }
    else if (studRank > 1)
    {
        return (rAge(studRank - 1) + 2);
    }
    /*end_edit*/
}