/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
#include <string.h>
struct account
{
    struct
    {
        char lastName[10];
        char firstName[10];
    } names;
    int accountNum;
    double balance;
};
void nextCustomer(struct account *acct);
void printCustomer(struct account acct);
int main()
{
    struct account record;
    int flag = 0;

    do
    {
        nextCustomer(&record);
        if ((strcmp(record.names.firstName, "End") == 0) &&
            (strcmp(record.names.lastName, "Customer") == 0))
            flag = 1;
        if (flag != 1)
            printCustomer(record);
    } while (flag != 1);
}
void nextCustomer(struct account *acct)
{
    /*edit*/
    /* Write your code here */
    char last_name[80], *p;
    printf("Please enter customer's last name: ");
    fgets(last_name, 80, stdin);
    if(p=strchr(last_name, '\n')) {
        *p = '\0';
        p=NULL;
    }
    strcpy(acct->names.lastName, last_name);
    char first_name[80], *q;
    printf("Please enter customer's first name: ");
    fgets(first_name, 80, stdin);
    if(q=strchr(first_name, '\n')) {
        *q = '\0';
        q=NULL;
    }
    strcpy(acct->names.firstName, first_name);
    printf("Please enter customer's account number: ");
    scanf(" %d", &acct->accountNum);
    printf("Please enter customer's balance: ");
    scanf(" %lf", &acct->balance);
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
    /*end_edit*/
}
void printCustomer(struct account acct)
{
    /*edit*/
    /* Write your code here */
    printf("Customer record:\n");
    printf("%s %s %d %.2f \n", acct.names.firstName, acct.names.lastName, acct.accountNum, acct.balance);
    /*end_edit*/
}