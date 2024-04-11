import numpy as np

# Given parameters
s1 = -0.2796 - 1.5228j
s2 = -0.6751 - 0.6308j
s3 = -0.6751 + 0.6308j
s4 = -0.2796 + 1.5228j
epsilon = 0.3043
Omega_Lp = 1.4775

# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 1.9552

# Define parameters for transformation
B = 0.094
Omega0 = 0.4404
# Perform transformation to get s_L
s_L = (1j * 0.5913)**2 + Omega0**2
s_L /= B * (1j * 0.5913)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
