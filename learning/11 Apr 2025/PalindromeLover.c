#include <stdio.h>

int palindrome_check(int N, int* A) {
	if(N%2 == 1) {
		return 1;
	}
	int num_0 = 0;
	int num_1 = 0;
	for(int k=0; k<N; k++) {
		if(A[k] == 0) {
			num_0 += 1;
		}else{
			num_1 += 1;
		}
	}
	if(N%2 == 0) {
		if(num_0%2 == 0 && num_1%2 == 0) {
			return 1;
		}else{
			return 0;
		}
	}
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		int N;
		scanf("%d", &N);
		int A[N];
		for(int j=0; j<N; j++) {
            scanf("%d", &A[j]);
			A[j] = A[j]%2;
        }
		int test = palindrome_check(N, A);
		printf("%d\n", test);
	} 
}

