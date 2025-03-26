#include <stdio.h>
#include <string.h>

int main(){
	char inputted[300], *p;
    fgets(inputted, 300, stdin);
    if(p=strchr(inputted, '\n')) {
        *p = '\0';
    }
    int num_of_z = 0;
    int num_of_o = 0;
    int pos = 0;
    while(inputted[pos] != '\0') {
        if(inputted[pos] == 'z' || inputted[pos] == 'Z') {
            num_of_z += 1;
        }else if(inputted[pos] == 'o' || inputted[pos] == 'O') {
            num_of_o += 1;
        }else{
            printf("No");
            return 0;
        }
        pos++;
    }
    if(num_of_o == 2 * num_of_z) {
        printf("Yes");
    }else{
        printf("No");
    }
    return 0;
}