import matplotlib.pyplot as plt
distances = []
wavelengths = []
with open("max_wavelength_data.txt", "r") as file:
    for line in file:
        distance, wavelength = map(float, line.split())
        distances.append(distance)
        wavelengths.append(wavelength)
plt.plot(distances, wavelengths)
plt.xlabel('d(km)')
plt.ylabel('$\lambda(cm)$')
plt.grid(True)
distance_40 = 40
max_wavelength_40 = wavelengths[20]
plt.scatter(distance_40, max_wavelength_40, color='red', label='Distance = 40 km')
plt.annotate(f'Distance = 40 km\nMax: ({distance_40:.2f}, {max_wavelength_40:.2f})',
             xy=(distance_40, max_wavelength_40),
             xytext=(distance_40 + 5, max_wavelength_40 - 0.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.legend()
plt.savefig('figs/fig2.png')
plt.show()

