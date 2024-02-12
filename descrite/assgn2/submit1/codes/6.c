#include <stdio.h>
#include <stdlib.h>


#define MIN_DISTANCE 20    // Minimum distance between towers in km
#define MAX_DISTANCE 100  // Maximum distance between towers in km

double max_wavelength(double distance) {
     double z_f = distance*5;
     double wavelength = (50*50)/z_f;
     return wavelength;
}

int main() {
    FILE *outputFile = fopen("max_wavelength_data.txt", "w"); // Open file for writing

    if (outputFile) {
        for (int distance = MIN_DISTANCE; distance <= MAX_DISTANCE; distance++) {
            double wavelength = max_wavelength(distance);
            fprintf(outputFile, "%d %lf\n", distance, wavelength);
        }

        fclose(outputFile);
    } else {
        printf("Error: Failed to open output file\n");
        return 1;
    }

    return 0;
}

