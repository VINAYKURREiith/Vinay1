import matplotlib.pyplot as plt
import math as math
def generate_gp(first_term, common_ratio, num_terms):
    gp_sequence = [first_term * common_ratio**n for n in range(num_terms)]
    return gp_sequence
first_term = math.sqrt(7)
common_ratio = math.sqrt(3)
num_terms = 10
gp_result = generate_gp(first_term, common_ratio, num_terms)
plt.plot(range(0, num_terms), gp_result, marker='o', linestyle='-', color='b',label='Line  plot')
plt.stem(range(0, num_terms), gp_result, markerfmt='r^', linefmt=':', basefmt='b',label='Stem  plot')
plt.title('Geometric Progression')
plt.xlabel('Term')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()
