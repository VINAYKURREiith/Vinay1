import numpy as np
import matplotlib.pyplot as plt
height_of_hill = 50  
distances_between_towers = np.linspace(20, 100, 1000)  
def max_wavelength(distance):
    z_f= distance*5
    wavelength = (height_of_hill**2)/(z_f)
    return wavelength
max_wavelengths = max_wavelength(distances_between_towers)
plt.figure(figsize=(10, 6))
plt.plot(distances_between_towers, max_wavelengths, color='blue')
plt.xlabel('d(km)')
plt.ylabel('$\lambda(cm)$')
plt.grid(True)
distance_40 = 40
max_wavelength_40 = max_wavelength(distance_40)
plt.scatter(distance_40, max_wavelength_40, color='red', label='Distance = 40 km')
plt.annotate(f'Distance = 40 km\nMax: ({distance_40:.2f}, {max_wavelength_40:.2f})',
             xy=(distance_40, max_wavelength_40),
             xytext=(distance_40 + 5, max_wavelength_40 - 0.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.legend()
plt.savefig('fig/fig2.png')
plt.show()
