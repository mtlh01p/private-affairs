	/*edit*/

/*custom header*/

	/*end_edit*/
#include <stdio.h>
#include <string.h>
char *sweepSpace(char *str);
int main()
{
   char str[80], *p;
 
   printf("Enter the string: \n");
   fgets(str, 80, stdin);
   if (p=strchr(str,'\n')) *p = '\0'; 
   printf("sweepSpace(): %s\n", sweepSpace(str));
   return 0;
}
char *sweepSpace(char *str)  
{
	/*edit*/
   /* Write your code here */
   int i, j=0;
   int a = strlen(str);
   for(i=0; i<a; i++) {
    if(str[i] != ' ' && str[i] != '\0') {
        str[j++] = str[i];
    }
   }
    str[j] = '\0';
    return(str);
	/*end_edit*/
}