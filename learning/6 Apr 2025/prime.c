#include <stdio.h>
#include <math.h>

int isprime(int num) {
	if(num != 2) {
		for(int i=2; i<=sqrt(num); i++) {
			if(num % i == 0) {
				return 0;
			} 
		}
	}
	return 1;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		int X;
		scanf("%d", &X);
		int divisors[79000];
		int d_track = 0;
		for(int i=2; i<1000000; i++) {
			if(isprime(i)) {
				divisors[d_track] = i;
				d_track++;
			}
		}
		if(X == 2){
			printf("500000\n");
		}else{
			int to_print = 0;
			for(int i=2; i<=1000000; i++) {
				int min = 0;
				for(int j=0; j<79000; j++) {
					if(i%divisors[j] == 0) {
						min = divisors[j];
						break;
					}
				}
				if(min == X) {
					to_print += 1;
				}
			}
			printf("%d\n", to_print);
		}
	}
	return 0;
}
