#include <stdio.h>
#include <string.h>

int main(){
	int N;
	scanf("%d", &N);
	while(getchar() != '\n');
	char f[N][11];
	for(int i=0; i<N; i++) {
		scanf("%s", f[i]);
		if(i==0) {
			printf("0\n");
		}else{
			int found = 0;
			for(int j=0; j<i; j++) {
				if(strcmp(f[j], f[i]) < 0) {
					found++;
				}
			}
			printf("%d\n", found);
		}
	}
	return 0;
}
