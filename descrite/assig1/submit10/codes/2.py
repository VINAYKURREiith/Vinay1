import matplotlib.pyplot as plt

def plot_gp(gp_sequence):
    plt.stem(range(len(gp_sequence)), gp_sequence, markerfmt='r^', linefmt='-', basefmt='b', label='Stem plot')
    plt.scatter(omega_40, capacitance_40, color='red', label='$\omega$ = 100$\pi$ rads/s\n C = 1.45 mF')
    plt.title('Geometric Progression')
    plt.xlabel('Term')
    plt.ylabel('Value')
    plt.grid(True)
    plt.legend()
    plt.savefig('fig2.png')
    plt.show()

# Read values from the file
with open('gp_values.txt', 'r') as file:
    gp_values = [float(line.strip()) for line in file]
    
with open('gp_sum_values.txt', 'r') as file:
    gp_sum_values = [float(line.strip()) for line in file]
    
    
plt.stem(range(len(gp_values)), gp_values, markerfmt='r^', linefmt='-', basefmt='b', label='Stem plot')
plt.scatter(range(len(gp_sum_values)), gp_sum_values, color='black', marker='o',label='y(n) using formulae')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)
plt.legend()
plt.savefig('fig2.png')
plt.show()
