#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main() {
    float a=sqrt(7), r= sqrt(3);
    for(int n=1; n<15;n++)   {
     float sum = a * (pow(r,n)-1) / ( r - 1);
    printf("y(%d) = %f\n",n-1 ,sum);
    }
    return 0;
}
