#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(){
	int N;
	scanf("%d", &N);
	int nums[N];
	int nums_c = 0;
	char inputted[40010], *p;
    while (getchar() != '\n');
    fgets(inputted, 40010, stdin);
    if ((p = strchr(inputted, '\n'))) {
        *p = '\0';
    }
    char *token = strtok(inputted, " ");
    while (token != NULL) {
        nums[nums_c++] = atoi(token);
        token = strtok(NULL, " ");
    }
	int good = 0;
	for(int i=0; i<nums_c; i++) {
		int end = i;
		while(end < nums_c) {
			int sums = 0;
			for(int j=i; j<=end; j++) {
				sums += nums[j];
			}
			int root = (int)sqrt(sums);
			if(root*root==sums) {
				good++;
			}
			end++;
		}
	}
	printf("%d", good);
	return 0;
}