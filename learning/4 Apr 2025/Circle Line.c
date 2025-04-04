#include<stdio.h>
#include<stdbool.h>
#include<malloc.h>

long long solve (int N, int start, int finish, int* Ticket_cost) {
    // Write your code here
    long cost_left = 0;
    long cur = start;
    long k = (cur-1);
    while(cur != finish) {
        if(cur <= N) {
            cost_left += Ticket_cost[k];
            k = (k + 1) % N;
            cur = (cur % N) + 1;
        }
    }
    long cost_right = 0;
    cur = start;
    k = (cur-1);
    while(cur != finish) {
        if(cur >= 1) {
            k = (k - 1 + N) % N;
            cost_right += Ticket_cost[k];
            cur = (cur + N - 2) % N + 1;
        }
    }
    if(cost_left < cost_right) {
        return(cost_left);
    }else{
        return(cost_right);
    }
}

int main() {
    int N;
    scanf("%d", &N);
    int start;
    scanf("%d", &start);
    int finish;
    scanf("%d", &finish);
    int i_Ticket_cost;
    int *Ticket_cost = (int *)malloc(sizeof(int)*(N));
    for(i_Ticket_cost = 0; i_Ticket_cost < N; i_Ticket_cost++)
    	scanf("%d", &Ticket_cost[i_Ticket_cost]);

    long long out_ = solve(N, start, finish, Ticket_cost);
    printf("%lld", out_);
}