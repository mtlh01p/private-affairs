#include <stdio.h>
#include <math.h>

int main(){
	int num_in;
	scanf("%d", &num_in);
	int nums[num_in];
	int diffs[num_in];
	diffs[0] = 0;
	scanf("%d", &nums[0]);
    int tracker = 0;
	for(int i=1; i<num_in; i++) {
		scanf("%d", &nums[i]);
		diffs[i] = abs(nums[i] - nums[0]);
        tracker = i+1;
	}
    int K[500];
    int p = 0;
	for(int i=2; i<=diffs[1]; i++) {
        if(diffs[1]%i == 0) {
            int validity = 1;
            for(int j=2; j<tracker; j++) {
                if(diffs[j]%i != 0) {
                    validity = 0;
                    break;
                }
            }
            if(validity) {
                K[p] = i;
                p++;
            }
        }
    }
    for(int i=0; i<p; i++) {
        printf("%d ", K[i]);
    }
    return 0;
}