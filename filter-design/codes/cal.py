from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.5172
B_val =0.1141

# Define s_L in terms of s, omega0, and B
s_L = (s**2 + omega0_val**2) / (B_val * s)

# Given roots
s1 = -0.3320 - 1.5755j
s2 = -0.8015 - 0.6526j
s3 = -0.8015 + 0.6526j
s4 = -0.3320 + 1.5755j

# Define the given polynomial expression
polynomial_expr = 17.985 / ((s_L - s1) * (s_L - s2) * (s_L - s3) * (s_L - s4))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
