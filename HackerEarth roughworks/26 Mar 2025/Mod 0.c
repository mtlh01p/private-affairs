#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(){
	int no_of_data = 0;
    scanf("%d", &no_of_data);
    while (getchar() != '\n');
    char inputted[1000], *p;
    fgets(inputted, 1000, stdin);
    if(p=strchr(inputted, '\n')) {
        *p = '\0';
    }
    int list_of_nums[no_of_data];
    int indexing = 0;
    int pos = 0;
    int prev = 0;
    int done = 0;
    while(done == 0) {
        if(inputted[pos] == ' ' || inputted[pos] == '\0') {
            if(inputted[pos] == '\0') {
                done = 1;
            }
            char temp[pos-prev+1];
            int pos2 = 0;
            for(int i=prev; i<pos; i++) {
                temp[pos2] = inputted[i];
                pos2++;
            }
            temp[pos-prev] = '\0';
            list_of_nums[indexing] = atoi(temp)%10;
            indexing++;
            prev = pos+1;
        }
        pos++;
    }
    int num_to_eval = 0;
    for(int i=0; i<no_of_data; i++) {
        num_to_eval += (list_of_nums[i] * pow(10, no_of_data-1-i));
    }
    if(num_to_eval%10 == 0) {
        printf("Yes");
    }else{
        printf("No");
    }
    return 0;
}