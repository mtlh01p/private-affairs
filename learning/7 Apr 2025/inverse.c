#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		int size;
		scanf("%d", &size);
		int nums[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                scanf("%d", &nums[i][j]);
            }
        }
		long occs = 0;
		for(int i=0; i<size; i++) {
			for(int j=0; j<size; j++) {
				for(int p=i; p<size; p++) {
					for(int q=j; q<size; q++) {
						if(nums[i][j] > nums[p][q]) {
							occs++;
						}
					}
				}
			}
		}
		printf("%ld\n", occs);
	}
	return 0;
}