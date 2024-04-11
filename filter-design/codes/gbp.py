import numpy as np

# Given parameters
s1 = -0.3320 - 1.5755j
s2 = -0.8015 - 0.6526j
s3 = -0.8015 + 0.6526j
s4 = -0.3320 + 1.5755j
epsilon = 0.2145
Omega_Lp = 1.4682

# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 0.4166

# Define parameters for transformation
B = 0.1107
Omega0 = 0.644

# Perform transformation to get s_L
s_L = (1j * 0.5913)**2 + Omega0**2
s_L /= B * (1j * 0.5913)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
