#include <stdio.h>
#include <math.h>

#define NUM_POINTS 1000

double max_wavelength(double distance);

int main() {
    double height_of_hill = 50.0;
    double distances_between_towers[NUM_POINTS];
    double max_wavelengths[NUM_POINTS];

    // Generate distances between towers from 20 km to 100 km
    for (int i = 0; i < NUM_POINTS; i++) {
        distances_between_towers[i] = 20.0 + (80.0 / NUM_POINTS) * i;
    }

    // Calculate max wavelength for each distance
    for (int i = 0; i < NUM_POINTS; i++) {
        max_wavelengths[i] = max_wavelength(distances_between_towers[i]);
    }

    // Print the results
    printf("Distance (km)\tMax Wavelength (cm)\n");
    for (int i = 0; i < NUM_POINTS; i++) {
        printf("%.2f\t\t%.2f\n", distances_between_towers[i], max_wavelengths[i]);
    }

    return 0;
}

double max_wavelength(double distance) {
    double z_f = distance * 5.0;
    double wavelength = (50.0 * 50.0) / z_f;
    return wavelength;
}

