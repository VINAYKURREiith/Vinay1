import numpy as np
def find_sum_of_gp_terms(first_term, common_ratio, number_of_terms):
        gp_sum = 0
        for i in range(number_of_terms):
            term = first_term * common_ratio**i
            gp_sum += term
            print(f"Term {i + 1}:  {gp_sum:.2f}")
        return gp_sum

def main():
    first_term = np.sqrt(7)
    common_ratio = np.sqrt(3)
    number_of_terms = 15

    sum_of_terms = find_sum_of_gp_terms(first_term, common_ratio, number_of_terms)

  #  print(f"\nSum of {number_of_terms} terms in the geometric progression: {sum_of_terms:.2f}")

if __name__ == "__main__":
    main()

