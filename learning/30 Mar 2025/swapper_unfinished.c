#include <stdio.h>
#include <string.h>

int main(){
	int testcases;
	scanf("%d", &testcases);
	while(getchar() != '\n');
	for(int i=0; i<testcases; i++) {
		int no_of_char;
		int possible = 1;
		scanf("%d", &no_of_char);
		while(getchar() != '\n');
		char s[no_of_char+1], *p;
		char t[no_of_char+1], *q;
		fgets(s, no_of_char, stdin);
		if(p=strchr(s, '\n')) {
			*p = '\0';
		}
		while(getchar() != '\n');
		fgets(t, no_of_char, stdin);
		if(q=strchr(t, '\n')) {
			*q = '\0';
		}
		int avail_index[no_of_char];
		int k=0;
		for(int j=0; j<no_of_char; j++) {
			if(s[j] != t[j]) {
				if(strchr(t, s[j]) || s[j] == '?') {
					avail_index[k] = j;
					k++;
				}else{
					possible = 0;
					break;
				}
			}
		}
		if(possible) {
			for(int j=0; j<k; j++) {
				if(avail_index[j] < 10000) {
					//avail_index[j]
					char dest = t[avail_index[j]];
					if(s[avail_index[j]] != '?') {
						int replaced = 0;
						for(int n=j+1; n<k; n++) {
							//avail_index[n]
							if(s[avail_index[n]] == dest) {
								char left = s[avail_index[n]];
								char right = dest;
								s[avail_index[j]] = left;
								s[avail_index[n]] = right;
								replaced = 1;
								break;
							}
						}
						if(!replaced) {
							printf("No\n");
							return 0;
						}
					}else{
						s[avail_index[j]] = dest;
						avail_index[j] = 10001;
					}
				}
			}
			printf("Yes\n");
			return 0;
		}else{
			printf("No\n");
			return 0;
		}
	}
}