#include <stdio.h>
#include <math.h>

int countBits(long num) {
    if(num == 0) return 1;
    return(int)(log2(num))+1;
}

int main(){
	int num;
	scanf("%d", &num);
	for(int i=0; i<num; i++) {
		long X;
		scanf("%ld", &X);
		long ans = 0;
		for(long j=1; j<=X; j++) {
			int j_bits = countBits(j);
			long result = X/j;
			int result_bits = countBits(result);
			if(j_bits >= result_bits) {
				ans++;
			}
		}
		printf("%ld\n", ans);
	}
}