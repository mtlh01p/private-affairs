/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
#include <string.h>
void extractFirstChar(char *str1, char *str2);
int main()
{
    char str1[80], str2[80], *p;

    printf("Enter a string: \n");
    fgets(str1, 80, stdin);
    if (p = strchr(str1, '\n'))
        *p = '\0';
    extractFirstChar(str1, str2);
    printf("extractFirstChar(): %s\n", str2);
    return 0;
}
void extractFirstChar(char *str1, char *str2)
{
    /*edit*/
    /* Write your code here */
    int indexer = 0;
    while(*(str1+indexer) == ' ') {
        indexer += 1;
    }
    *str2 = *(str1+indexer);
    *(str2+1) = '\0';
    /*end_edit*/
}