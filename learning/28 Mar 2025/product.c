#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

long main(){
	int num;
	scanf("%d", &num);
    while(getchar() != '\n');
	char inputted[10000], *p;
	fgets(inputted, 10000, stdin);
	if(p=strchr(inputted, '\n')) {
		*p = '\0';
	}
	long list_of_ints[num];
	int indexed = 0;
	int prev = 0;
	for(int i=0; i<=strlen(inputted); i++) {
		if(inputted[i] == ' ' || inputted[i] == '\0') {
			char wreck[i-prev+1];
            int k = 0;
			for(int j=prev; j<i; j++) {
				wreck[k++] = inputted[j];
			}
			wreck[k] = '\0';
			list_of_ints[indexed] = atol(wreck);
			indexed++;
			prev = i+1;
		}
	}
	long result = 1;
    long modder = pow(10, 9) + 7;
    for(int i=0; i<num; i++) {
        result = (result*list_of_ints[i]) % modder;
    }
    printf("%ld", result);
	return 0;
}