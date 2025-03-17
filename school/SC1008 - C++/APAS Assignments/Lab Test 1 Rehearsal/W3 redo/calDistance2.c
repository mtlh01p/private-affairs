#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
void inputXY(double *x1, double *y1, double *x2, double *y2); 
void outputResult(double dist); 
double calDistance1(double x1, double y1, double x2, double y2); 
void calDistance2(double x1, double y1, double x2, double y2, double *dist);

int main() {
    double x1, y1, x2, y2, distance=-1;  
    inputXY(&x1, &y1, &x2, &y2);      
    printf("%.2f %.2f %.2f %.2f \n", x1, y1, x2, y2); 
    distance = calDistance1(x1, y1, x2, y2);   
    printf("calDistance1(): ");    
    outputResult(distance); 
    calDistance2(x1, y1, x2, y2, &distance);
    printf("calDistance2(): ");    
    outputResult(distance);             
    return 0;
}

void inputXY(double *x1, double *y1, double *x2, double *y2) {
    printf("Input x1 y1 x2 y2: \n");
    scanf("%lf %lf %lf %lf", x1, y1, x2, y2);
}

void outputResult(double dist) {
    printf("%.2f\n", dist);
}
double calDistance1(double x1, double y1, double x2, double y2) {
    double width = x2-x1;
    double height = y2-y1;
    double area = width * height;
    return(area);
}
void calDistance2(double x1, double y1, double x2, double y2, double *dist) {
    *dist = calDistance1(x1, y1, x2, y2);
}