#include <stdio.h>

int main() {
    int hh, mm;
    scanf("%d:%d", &hh, &mm);

    int totalMinutes = hh * 60 + mm;
    int overlapCount = 1;

    for (int currentMinute = 1; currentMinute <= totalMinutes; currentMinute++) {
        int hourHandPosition = hh/12 * 60;
        int minuteHandPosition = currentMinute % 60;

        if (hourHandPosition == minuteHandPosition) {
            overlapCount++;
        }
    }

    printf("%d\n", overlapCount);

    return 0;
}
