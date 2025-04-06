#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int N, K;
	scanf("%d %d", &N, &K);
	int nums[N];
	int nums_c = 0;
	char inputted[1100010], *p;
    while (getchar() != '\n');
    fgets(inputted, 1100010, stdin);
    if ((p = strchr(inputted, '\n'))) {
        *p = '\0';
    }
    char *token = strtok(inputted, " ");
    while (token != NULL) {
        nums[nums_c++] = atoi(token);
        token = strtok(NULL, " ");
    }
	int sums = 0;
	int added = 0;
	int start = 0;
	int end = nums_c-1;
	int first_phase = 1;
	while(added < K) {
		if(first_phase) {
			if(nums[start] >= nums[end]) {
				sums += nums[start];
				start++;
				added++;
			}else{
				first_phase = 0;
			}
		}else{
			sums += nums[end];
			end--;
			added++;
		}
	}
	printf("%d", sums);
}