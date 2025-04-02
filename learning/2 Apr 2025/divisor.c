#include <stdio.h>

int main(){
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		long long num;
		scanf("%lld", &num);
		long long divisor = 0;
		long long divided = 1;
		for(long long j=1; j<=num; j++) {
			divisor += j;
			divided *= j;
		}
		if(divided % divisor == 0) {
			printf("YES\n");
		}else{
			printf("NO\n");
		}
	}
}
