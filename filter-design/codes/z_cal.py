import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s =17.985*s**4/(5900.07350597734*s**8 + 1526.14074340158*s**7 + 6675.92495680965*s**6 + 1267.34693693741*s**5 + 2729.98575911186*s**4 + 339.010033467501*s**3 + 477.689297367658*s**2 + 29.2109501864183*s + 30.2082489698599)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


