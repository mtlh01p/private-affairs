#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
int isprime(int num) {
    if (num <= 1) {
        return 0;
    }
    if (num == 2) {
        return 1;
    }
    if (num % 2 == 0) {
        return 0;
    }
    for (int i = 3; i <= sqrt(num); i += 2) {
        if (num % i == 0) {
            return 0;
        }
    }
    return 1;
}


int main(){
	int num;
	scanf("%d", &num);
	while(getchar() != '\n');
    char *p;
    char *inputted = (char *)malloc(8000010 * sizeof(char));
    int *nums = (int *)malloc(1000000 * sizeof(int));
	fgets(inputted, 8000010, stdin);
	if(p=strchr(inputted, '\n')) {
		*p = '\0';
	}
	int prev = 0;
	int pos = 0;
    int len = strlen(inputted);
	for(int i=0; i<=len; i++) {
		if(inputted[i] == ' ' || inputted[i] == '\0') {
			char temp[10];
			int k = 0;
			for(int j=prev; j<i; j++) {
				temp[k] = inputted[j];
				k++;
			}
			temp[k] = '\0';
			nums[pos] = atoi(temp);
			pos++;
			prev = i+1;
		}
	}
	int checking = 0;
	int max = 0;
	int min = 0;
	while(checking < pos) {
        if(nums[checking] %2 != 0 || nums[checking] == 2) {
		    if(isprime(nums[checking])) {
			    if(min == 0 || nums[checking] < min) {
				    min = nums[checking];
			    }
			    if(nums[checking] > max) {
			    	max = nums[checking];
			    }
		    }
        }
		checking++;
	}
	if(max != 0 && min != 0) {
		printf("%d", (max-min));
	}else{
		printf("-%d", 1);
	}
    free(inputted);
    free(nums);
    return 0;
}