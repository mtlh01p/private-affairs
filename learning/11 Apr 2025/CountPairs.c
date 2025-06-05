#include <stdio.h>

int main(){
	int T;
	scanf("%d", &T);
	for(int a=0; a<T; a++) {
		int N;
		scanf("%d", &N);
		int A[N];
		for(int b=0; b<N; b++) {
            scanf("%d", &A[b]);
        }
		int pairs = 0;
		for(int i=0; i<N-1; i++) {
			for(int j=i+1; j<N; j++) {
				int min = 0;
				if(A[i] <= A[j]) {
					min = A[i];
				}else{
					min = A[j];
				}
				if((A[i] ^ A[j]) >= min) {
					pairs += 1;
				}
			}
		}
		printf("%d\n", pairs);
	}
}
