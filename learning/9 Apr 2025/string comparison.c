#include <stdio.h>
#include <string.h>

int main(){
	int S;
	char tel[26];
	char suff[26][26] = {0};
	scanf("%s %d", &tel, &S);
	for(int i=0; i<strlen(tel); i++) {
		for(int j=i; j<strlen(tel); j++) {
			suff[i][j-i] = tel[j];
		}
	}
	for(int i=0; i<strlen(tel); i++) {
		for(int j=i; j<strlen(tel); j++) {
			if(strcmp(suff[i], suff[j]) > 0) {
				char left[26];
				strcpy(left, suff[i]);
				char right[26];
				strcpy(right, suff[j]);
				strcpy(suff[i], right);
				strcpy(suff[j], left);
			}
		}
	}
	printf("%s", suff[S-1]);
	return 0;
}