#include <stdio.h>

int main(){
	int num_of_testcases;
	scanf("%d", &num_of_testcases);
    for(int i=0; i<num_of_testcases; i++) {
        int green_pri = 0;
        int purple_pri = 0;
        scanf("%d %d", &green_pri, &purple_pri);
        int no_of_part = 0;
        scanf("%d", &no_of_part);
        int problem1[no_of_part];
        int problem2[no_of_part];
        for(int j=0; j<no_of_part; j++) {
            scanf("%d %d", &problem1[j], &problem2[j]);
        }
        int min_pay = 0;
        for(int j=0; j<2; j++) {
            int problem1_fixed = 0;
            int problem2_fixed = 0;
            for(int k=0; k<no_of_part; k++) {
                problem1_fixed += problem1[k];
                problem2_fixed += problem2[k];
            }
            int payway = 0;
            if(min_pay == 0) {
                payway = problem1_fixed * green_pri + problem2_fixed * purple_pri;
                min_pay = payway;
            }else{
                payway = problem1_fixed * purple_pri + problem2_fixed * green_pri;
                if(payway < min_pay) {
                    min_pay = payway;
                }
            }
        }
        printf("%d\n", min_pay);
    }
}