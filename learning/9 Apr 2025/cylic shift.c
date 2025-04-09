#include <stdio.h>
#include <string.h>

int main(){
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		int N, K;
		scanf("%d %d", &N, &K);
		while(getchar() != '\n');
		char streng[N+1];
		scanf("%s", &streng);
		char back = streng[0];
		for(int j=0; j<N-1; j++) {
			streng[j] = streng[j+1];
		}
		streng[N-1] = back;
		int times[K];
		int times_ind = 0;
		char shift[N+1];
		strcpy(shift, streng);
		int steps = 0;
		while(times_ind < K) {
			back = shift[0];
			for(int j=0; j<N-1; j++) {
				shift[j] = shift[j+1];
			}
			shift[N-1] = back;
			steps++;
			if(strcmp(shift, streng) == 0) {
				times[times_ind++] = steps;
				steps = 0;
				back = shift[0];
				for(int j=0; j<N-1; j++) {
					shift[j] = shift[j+1];
				}
				shift[N-1] = back;
			}
		}
		int sum = 0;
		for(int j=0; j<times_ind; j++) {
			sum += times[j];
		}
		printf("%d\n", sum);
	}
	return 0;
}
