#include<stdio.h>
#include<stdbool.h>
#include<malloc.h>

long long NotinRange (int* R, int* L, int n ) {
    long long sums = 0;
   for(int i=0; i<=1000000; i++) {
    int validity = 1;
    for(int j=0; j<n; j++) {
        if(i >= L[j] && i <= R[j]) {
            validity = 0;
            break;
        }
    }
    if(validity) {
        sums += i;
    }
   }
   return sums;
}

int main() {
    int n;
    scanf("%d", &n);
    int L[n],R[n];
    for(int i=0; i<n; i++)
    	scanf("%d %d", &L[i],&R[i]);
    
    long long out_ = NotinRange(R, L, n);
    printf("%lld", out_);
}