/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
#define M 10
void matShifting(int a[M][M], int b[M][M], int n);
int main()
{
    int a[M][M], b[M][M];
    int n, i, j;

    printf("Enter array (nxn) size (n<=10): \n");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("Enter row %d: \n", i);
        for (j = 0; j < n; j++)
            scanf("%d", &a[i][j]);
    }
    matShifting(a, b, n);
    printf("Array b: \n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
            printf("%d ", b[i][j]);
        printf("\n");
    }
    return 0;
}
void matShifting(int a[M][M], int b[M][M], int n)
{
    /*edit*/
    /* Write your code here */
    int i, j;
    for(i=0; i<n; i++) {
        for(j=0; j<n; j++) {
            if(j+1 < n) {
                b[i][j+1] = a[i][j];
            }else{
                b[i][0] = a[i][j];
            }
        }
    }
    /*end_edit*/
}