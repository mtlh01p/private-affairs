/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
#include <string.h>
int countWords(char *s);
int main()
{
    char str[80], *p;

    printf("Enter the string: \n");
    fgets(str, 80, stdin);
    if (p = strchr(str, '\n'))
        *p = '\0';
    printf("countWords(): %d", countWords(str));
    return 0;
}
int countWords(char *s)
{
    /*edit*/
    /* Write your code here */
    int numofwords = 0;
    int indexer = 1;
    if(*s != '\0' || *s != ' ') {
        numofwords += 1;
    }
    while(*(s+indexer) != '\0') {
        if(*(s+indexer) == ' ' && *(s+indexer+1) != ' ') {
            numofwords += 1;
        }
        indexer += 1;
    }
    return numofwords;
    /*end_edit*/
}