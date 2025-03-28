#include <stdio.h>

int main(){
	int l = 0;
	int r = 0;
	int k = 0;
	scanf("%d %d %d", &l, &r, &k);
	int nums = 0;
	for(int i=l; i<=r; i++) {
		if(i%k == 0) {
			nums++;
		}
	}
	printf("%d", nums);
}
