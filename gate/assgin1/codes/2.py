mport numpy as np
import matplotlib.pyplot as plt
freq_values = np.linspace(20, 100, 100)  
omega_values = 2*np.pi*freq_values
capacitance_values = (1000) / (2.2 * omega_values)
plt.plot(omega_values, capacitance_values)
plt.xlabel('Angular Frequency ($\omega$)')
plt.ylabel('Capacitance (mF)')
plt.grid(True)
omega_40 = 2*np.pi*50
capacitance_40 =  (1000) / (2.2 * omega_40)
plt.scatter(omega_40, capacitance_40, color='red', label='$\omega$ = 100$\pi$ rads/s\n C = 1.45 mF')
plt.legend()
plt.savefig('fig/fig3.png')
plt.show()
