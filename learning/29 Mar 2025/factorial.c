#include <stdio.h>

int main(){
	int num;
	scanf("%d", &num);
	int result = num;
	for(int i=(num-1); i>=1; i--) {
		result *= i;
	}
	printf("%d", result);
}