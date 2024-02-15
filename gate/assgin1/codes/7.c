#include <stdio.h>
#include <math.h>

#define R1 2.2  
#define R2 2.2  
#define L 7  
#define OMEGA (100 * M_PI) 
void calculate_Y_in(double C, double *real_part, double *imag_part) {
    double E=pow(R1,2) + pow((L * OMEGA),2);
    double F=pow(R2,2) +(1/pow((OMEGA * C),2));
    double a = R1/E;
    double b = R2/F;
    double c = (L * OMEGA)/E;
    double D= (1/(OMEGA * C))/F;
    *real_part =  a + b;
    *imag_part = D - c;
}

int main() {
    double C_values[1000]; 
    double Y_in_real[1000]; 
    double Y_in_imag[1000];  
    int i;
    for (i = 0; i < 1000; i++) {
        C_values[i] = 0 + i * (20 - 0.0001) / 999.0;
    }
FILE *outputFile = fopen("y_data.txt", "w"); 

    if (outputFile) {
        for (i = 0; i < 1000; i++) {
        calculate_Y_in(C_values[i], &Y_in_real[i], &Y_in_imag[i]);
            fprintf(outputFile, "%lf %lf\n", Y_in_real[i], Y_in_imag[i]);
        }

        fclose(outputFile);
    } else {
        printf("Error: Failed to open output file\n");
        return 1;
    }
    
    return 0;
}

