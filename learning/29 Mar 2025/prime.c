#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

int prime(int test){
    if(test <= 1) {
        return 0;
    }
    for(int i=2; i<=sqrt(test); i++) {
        if(test%i == 0) {
            return 0;
        }
    }
    return 1;
}

int main(){
	int num;
	scanf("%d", &num);
    while(getchar() != '\n');
    for(int i=0; i<num; i++) {
        int N;
        scanf("%d", &N);
        while(getchar() != '\n');
        char inputted[700000], *p;
        fgets(inputted, 700000, stdin);
        if(p=strchr(inputted, '\n')) {
            *p = '\0';
        }
        int list_of_nums[N];
        int s=0;
        int f=0;
        for(int a=0; a<=strlen(inputted); a++) {
            if(inputted[a] == ' ' || inputted[a] == '\0') {
                char temp[7];
                int q=0;
                for(int l=s; l<a; l++) {
                    temp[q] = inputted[l];
                    q++;
                }
                temp[q] = '\0';
                list_of_nums[f] = atoi(temp);
                f++;
                s = a+1;
            }
        }
        int triplets = 0;
        for(int a=0; a<(N-2); a++) {
            for(int b=(a+1); b<(N-1); b++) {
                for(int c=(b+1); c<N; c++) {
                    int testing = list_of_nums[a] * list_of_nums[b] * list_of_nums[c];
                    if(prime(testing)) {
                        triplets++;
                    }
                }
            }
        }
        printf("%d\n", triplets);
    }

	return 0;
}