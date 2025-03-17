/*edit*/

/*custom header*/
#include <stdbool.h>
/*end_edit*/
#include <stdio.h>
#include <string.h>
#define INIT_VALUE -1000
int palindrome(char *str);
int main()
{
    char str[80], *p;
    int result = INIT_VALUE;

    printf("Enter a string: \n");
    fgets(str, 80, stdin);
    if (p = strchr(str, '\n'))
        *p = '\0';
    result = palindrome(str);
    if (result == 1)
        printf("palindrome(): A palindrome\n");
    else if (result == 0)
        printf("palindrome(): Not a palindrome\n");
    else
        printf("An error\n");
    return 0;
}
int palindrome(char *str)
{
    /*edit*/
    /* Write your code here */
    int indexer = 0;
    while(*(str+indexer) != '\0') {
        indexer += 1;
    }
    char str_comp[indexer+1];
    str_comp[indexer] = '\0';
    for(int i=0; i<indexer; i++) {
        str_comp[indexer-1-i] = *(str+i);
    }
    bool palindrome = true;
    for(int j=0; j<indexer; j++) {
        if(str_comp[j] != *(str+j)) {
            palindrome = false;
            break;
        }
    }
    if(palindrome) {
        return(1);
    }else{
        return(0);
    }
    /*end_edit*/
}