#include <stdio.h>

int main(){
	long L = 0;
	long R = 0;
	scanf("%ld %ld", &L, &R);
	for(long i=L+1; i<=R; i++) {
		L = L^i;
	}
	if(L%2 == 0) {
		printf("even");
	}else{
		printf("odd");
	}
	return 0;
}