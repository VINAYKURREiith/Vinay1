import numpy as np
import matplotlib.pyplot as plt
Y_in_reals = []
Y_in_imags = []
with open("y_data.txt", "r") as file:
    for line in file:
        Y_in_real, Y_in_imag = map(float, line.split())
        Y_in_reals.append(Y_in_real)
        Y_in_imags.append(Y_in_imag)
plt.plot(Y_in_reals, Y_in_imags)
plt.xlabel('Real(Y_in)')
plt.ylabel('Imaginary(Y_in)')
plt.grid(True)
plt.scatter(0.454545, 0, color='red', label='Touching real axis')
plt.annotate(f'Real(Y_in) = 0.454545\nMax: (0.454545, 0)',
             xy=(0.454545,0),
             xytext=(0.45449, 0),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.legend()
plt.savefig('figs/fig2.png')
plt.show()

