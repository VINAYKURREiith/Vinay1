import matplotlib.pyplot as plt
import numpy as np
import math as math

def geometric_progression_sum(a, r, n):
    # Function to calculate the sum of a geometric progression
    return a * (1 - r**n) / (1 - r)

def plot_gp_sum(a, r, n):
    terms = np.arange(0, n)
    sums = [geometric_progression_sum(a, r, i) for i in terms]

    plt.stem(terms, sums, markerfmt='r^', linefmt='-', basefmt='b',label='Stem  plot')
    plt.xlabel('$n$')
    plt.ylabel('$y(n)$')
    plt.grid(True)
    plt.savefig('fig/fig1.png')
    plt.show()

# Example usage:
a_value = math.sqrt(7)  # first term of the GP
r_value = math.sqrt(3)  # common ratio
n_terms = 10  # number of terms

plot_gp_sum(a_value, r_value, n_terms)

