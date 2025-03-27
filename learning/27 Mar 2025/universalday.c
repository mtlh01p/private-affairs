#include <stdio.h>

int main(){
    int done = 0;
    while(done == 0) {
        int inputted = 0;
        scanf("%d", &inputted);
        if(inputted == 42) {
            done = 1;
        }else{
            printf("%d\n", inputted);
        }
    }
	return 0;
}