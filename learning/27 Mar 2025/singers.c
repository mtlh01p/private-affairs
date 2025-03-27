#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(){
	int num;
	scanf(" %d", &num);
	while(getchar() != '\n');
	char inputted[100000], *p;
	fgets(inputted, 100000, stdin);
	if(p=strchr(inputted, '\n')) {
		*p = '\0';
	}
	int singers[10000];
	int singers_pos = 0;
	int votes[10000];
	for(int i=0; i<1000; i++) {
		singers[i] = 0;
		votes[i] = 0;
	}
	int prev = 0;
	for(int i=0; i<=strlen(inputted); i++) {
		if(inputted[i] == ' ' || inputted[i] == '\0') {
			char singer_temp[i-prev+1];
			for(int j=prev; j<i; j++) {
				singer_temp[j-prev] = inputted[j];
			}
			singer_temp[i-prev] = '\0';
			int search = atoi(singer_temp);
			if(singers_pos == 0) {
				singers[0] = search;
				votes[0] = 1;
				singers_pos++;
			}else{
				int found = 0;
				for(int j=0; j<singers_pos; j++) {
					if(singers[j] == search) {
						votes[j]++;
						found = 1;
						break;
					}
				}
				if(!found) {
					singers[singers_pos] = search;
					votes[singers_pos] = 1;
					singers_pos++;
				}
			}
			prev = i+1;
		}
		if(inputted[i] == '\0') {
			break;
		}
	}
	int max = 0;
	int nums = 0;
	int pos_eval = 0;
	while(votes[pos_eval] != 0) {
		if(votes[pos_eval] > max) {
			max = votes[pos_eval];
			nums = 1;
		}else if(votes[pos_eval] == max) {
			nums++;
		}
		pos_eval++;
	}
	printf("%d", nums);
}
