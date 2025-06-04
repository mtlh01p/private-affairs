#include<stdio.h>
#include<stdbool.h>
#include<malloc.h>
#include<math.h>

int solve (int N) {
    // Write your code here
    int good = -1;
    while(true) {
        if(pow(2, good+1) <= N) {
            good += 1;
        }else{
            break;
        }
    }
    return pow(2, good);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int t_i = 0; t_i < T; t_i++)
    {
        int N;
        scanf("%d", &N);

        int out_ = solve(N);
        printf("%d", out_);
        printf("\n");
    }
}
