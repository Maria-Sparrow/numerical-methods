def main():
    print("\tApproximate integration using Simpson's Rule")
    partitions = 10
    integrand = lambda x: x * (x ** 2 + 3) ** (1 / 2)
    antiderivative = lambda x: (x ** 2 + 3) ** (3 / 2) / 3
    lower_limit = 1
    upper_limit = 2

    integral = 0
    middle_point = (upper_limit - lower_limit) / (2 * partitions)
    integral += integrand(lower_limit) + integrand(upper_limit)
    for i in range(partitions):
        integral += 4 * integrand(lower_limit + (2 * i - 1) * middle_point)
    for i in range(partitions - 1):
        integral += 2 * integrand(lower_limit + 2 * i * middle_point)
    integral *= middle_point / 3
    print("Result: ", integral)
    print("Verification:")
    print("{} ~= {}".format(integral, antiderivative(upper_limit) - antiderivative(lower_limit)))


main()
