#include<stdio.h>
#include<stdbool.h>
#include<malloc.h>
#include<string.h>

int solve (char* S, char k) {
   int number = 0;
   int checking = strlen(S);
   for(int i=0; i<checking; i++) {
    if(S[i] == k) {
        number += 1;
    }
   }
   return number;
}

int main() {
    int T;
    scanf("%d", &T);

    for(int t_i = 0; t_i < T; t_i++)
    {
        char* S = (char*)malloc(200000 * sizeof(char));
        if (S == NULL) {
            perror("Failed to allocate memory for S");
            return 1;
        }
        scanf("\n%199999[^\n]", S);
        char k;
        scanf(" %c", &k);
        int out_ = solve(S, k);
        printf("%d\n", out_);
        free(S);
        S = NULL;
    }

    return 0;
}
