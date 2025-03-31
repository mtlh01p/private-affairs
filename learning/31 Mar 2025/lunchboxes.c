#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

long main(){
	long t;
	scanf("%d", &t);
	for(long i=0; i<t; i++) {
		long n, m;
		scanf("%d %d", &n, &m);
		long a[m];
        long track = 0;
        long possibilities = pow(2, m);
        long configs[possibilities][m]; 
        long track_config = 0;
        long configs_schsv[possibilities];
		while(getchar() != '\n');
		char inputted[100000], *p;
		fgets(inputted, 100000, stdin);
		if(p=strchr(inputted, '\n')) {
			*p = '\0';
		}
		long prev = 0;
		for(long j=0; j<=strlen(inputted); j++) {
			if(inputted[j] == ' ' || inputted[j] == '\0') {
				char temp[1000];
				long r = 0;
				for(long k=prev; k<j; k++) {
					temp[r++] = inputted[k];
				}
				temp[r] = '\0';
				a[track] = atoi(temp);
                track++;
				prev = j+1;
			}
		}
        for(long j=0; j<possibilities; j++) {
            long temp_config[m];
            long r = m-1;
            long test = j;
            long schsv = 0;
            for (long k = 0; k < m; k++) {
                temp_config[k] = (test >> (m - 1 - k)) & 1;
                if (temp_config[k] == 1) schsv++;
            }
            memcpy(configs[track_config], temp_config, sizeof(temp_config));
            configs_schsv[track_config] = schsv;
            track_config++;
        }
        long max_sch = 0;
        for(long j=0; j<track_config; j++) {
            long orders = 0;
            for(long k=0; k<m; k++) {
                orders += configs[j][k] * a[k];
            }
            if(orders <= n) {
                if(configs_schsv[j] > max_sch) {
                    max_sch = configs_schsv[j];
                }
            }
        }
        printf("%ld\n", max_sch);
	}
	return 0;
}
