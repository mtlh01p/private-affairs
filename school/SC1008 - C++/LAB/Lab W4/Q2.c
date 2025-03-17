/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
#define SIZE 3
void swap2Rows(int ar[][SIZE], int r1, int r2);
void swap2Cols(int ar[][SIZE], int c1, int c2);
void display(int ar[][SIZE]);
int main()
{
    int array[SIZE][SIZE];
    int row1, row2, col1, col2;
    int i, j;
    int choice;

    printf("Select one of the following options: \n");
    printf("1: getInput()\n");
    printf("2: swap2Rows()\n");
    printf("3: swap2Cols()\n");
    printf("4: display()\n");
    printf("5: exit()\n");
    do
    {
        printf("Enter your choice: \n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter the matrix (3x3): \n");
            for (i = 0; i < SIZE; i++)
                for (j = 0; j < SIZE; j++)
                    scanf("%d", &array[i][j]);
            break;
        case 2:
            printf("Enter two rows for swapping: \n");
            scanf("%d %d", &row1, &row2);
            swap2Rows(array, row1, row2);
            printf("The new array is: \n");
            display(array);
            break;
        case 3:
            printf("Enter two columns for swapping: \n");
            scanf("%d %d", &col1, &col2);
            swap2Cols(array, col1, col2);
            printf("The new array is: \n");
            display(array);
            break;
        case 4:
            display(array);
            break;
        }
    } while (choice < 5);
    return 0;
}
void display(int ar[][SIZE])
{
    int l, m;
    for (l = 0; l < SIZE; l++)
    {
        for (m = 0; m < SIZE; m++)
            printf("%d ", ar[l][m]);
        printf("\n");
    }
}
void swap2Rows(int ar[][SIZE], int r1, int r2)
{
    /*edit*/
    /* Write your code here */
    int swapper1[SIZE];
    int swapper2[SIZE];
    int i, j;
    for(i=0; i<SIZE; i++) {
        swapper1[i] = ar[r1][i];
    }
    for(j=0; j<SIZE; j++) {
        swapper2[j] = ar[r2][j];
    }
    for(i=0; i<SIZE; i++) {
        ar[r1][i] = swapper2[i];
    }
    for(j=0; j<SIZE; j++) {
        ar[r2][j] = swapper1[j];
    }
    /*end_edit*/
}
void swap2Cols(int ar[][SIZE], int c1, int c2)
{
    /*edit*/
    /* Write your code here */
    int swapper1[SIZE];
    int swapper2[SIZE];
    int i, j;
    for(i=0; i<SIZE; i++) {
        swapper1[i] = ar[i][c1];
    }
    for(j=0; j<SIZE; j++) {
        swapper2[j] = ar[j][c2];
    }
    for(i=0; i<SIZE; i++) {
        ar[i][c1] = swapper2[i];
    }
    for(j=0; j<SIZE; j++) {
        ar[j][c2] = swapper1[j];
    }
    /*end_edit*/
}