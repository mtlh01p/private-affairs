#include <stdio.h>
#include <math.h>
#include <stdbool.h>
int main() {
    int student_id, mark;
    char rank;
    bool Cont = true; 
    while(Cont) {
        printf("Enter Student ID: \n");
        scanf("%d", &student_id);
        if(student_id != -1) {
            printf("Enter Mark: \n");
            scanf("%d", &mark);
            if (mark >= 75) {
                rank = 'A';
            }else if(mark >= 65) {
                rank = 'B';
            }else if(mark >= 55) {
                rank = 'C';
            }else if(mark >= 45) {
                rank = 'D';
            }else if(mark >= 0) {
                rank = 'F';
            }
        printf("Grade = %c \n", rank);
        }else{
            Cont = false;
        }
    }
    return 0;
}