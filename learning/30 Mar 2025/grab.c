#include <stdio.h>

int main(){
	long D, OC, OF, OD, CS, CB, CM, CD;
	scanf("%ld", &D);
	scanf("%ld %ld %ld", &OC, &OF, &OD);
	scanf("%ld %ld %ld %ld", &CS, &CB, &CM, &CD);
	long online_cost = OC + (D-OF)*OD;
	long classic_cost = CB + D*CD + (D/CS)*CM;
	if(online_cost < classic_cost || online_cost == classic_cost) {
		printf("Online Taxi");
	}else{
		printf("Classic Taxi");
	}
	return 0;
}
