#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		int N, K;
		scanf("%d %d", &N, &K);
		K = K%N;
		int nums[N];
		int nums_c = 0;
		while(getchar() != '\n');
		char inputted[800010];
		fgets(inputted, 800010, stdin);
		char *token = strtok(inputted, " ");
		while(token != NULL) {
			nums[nums_c++] = atoi(token);
			token = strtok(NULL, " ");
		}
		for(int i=(N-K); i<N; i++) {
			printf("%d ", nums[i]);
		}
		for(int i=0; i<(N-K); i++) {
			printf("%d ", nums[i]);
		}
		printf("\n");
	}
	return 0;
}