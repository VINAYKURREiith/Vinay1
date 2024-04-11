import numpy as np
import matplotlib.pyplot as plt

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

G_LP = 1.9552
num = G_LP

Omega_p1 = 0.4899
Omega_p2 = 0.3959

Omega_s1 = 0.5177
Omega_s2 = 0.3764

# Define parameters for transformation
B = 0.094
Omega0 = 0.4404

# Perform transformation to get s_L
s_L = (1j * w)**2 + Omega0**2
s_L = s_L / (B * (1j * w))

# Band pass gain
G_bp = 6.6438

# Substitute s = jw into H(s)
H = G_bp * (num / np.polyval(den, s_L))

# Plot magnitude response for H(s)
plt.figure()
plt.plot(w, abs(H), linewidth=1)
plt.title('Band Pass Filter')
plt.xlabel('Analog Frequency ($\Omega$)')
plt.ylabel('|H_{a,BP}($\Omega$)|')
plt.grid(True)
plt.ylim(0, 1.2)
plt.savefig("fig4.png")
