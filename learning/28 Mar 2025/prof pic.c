#include <stdio.h>

int main(){
	int L = 0;
	int N = 0;
	scanf("%d", &L);
	scanf("%d", &N);
	for(int i=0; i<N; i++) {
		int W = 0;
		int H = 0;
		scanf("%d %d", &W, &H);
		if(W < L || H < L) {
			printf("UPLOAD ANOTHER\n");
		}else if(W != H) {
			printf("CROP IT\n");
		}else{
			printf("ACCEPTED\n");
		}
	}
	return 0;
}