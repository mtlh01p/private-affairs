#include <stdio.h>
#include <math.h>
int main() {
    int height, i, heightreached, j;
    char m[2];
    printf("Enter the height: \n");
    scanf("%d", &height);
    if (height != 0) {
        for(heightreached=1; heightreached<=height; heightreached++) {
            for(i=0; i<heightreached; i++) {
                j = heightreached % 3;
                if (j == 0) {
                    j = 3;
                }
                sprintf(m, "%d", j);
                printf("%s", m);
            }
            printf("\n");
        }
    }else{
        printf("You entered a height of 0!");
    }
    return 0;
}