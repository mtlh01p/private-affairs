#include <stdio.h>

int main(){
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		int N, p, q, r;
		int days = 0;
		scanf("%d %d %d %d", &N, &p, &q, &r);
		for(int j=1; j<=N; j++) {
			int taking_off = 0;
			if(j%p == 0) {
				taking_off++;
			}
			if(j%q == 0) {
				taking_off++;
			}
			if(j%r == 0) {
				taking_off++;
			}
			if(taking_off == 1) {
				days++;
			}
		}
		printf("%d\n", days);
	}
}