import numpy as np
import matplotlib.pyplot as plt

# Define the function for x(n)
def x_n(n):
    return 2*(np.cos(np.pi * n / 3) + 2 * np.cos(2 * np.pi * n / 3) + 3 * np.cos(np.pi * n)) + 2

# Generate values for n from 0 to 5
n_values = np.arange(0, 11)

# Compute x(n) for each value of n
x_values = x_n(n_values)

# Plot the stem plot
plt.stem(n_values, x_values)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('figs/fig.png')
plt.show()

