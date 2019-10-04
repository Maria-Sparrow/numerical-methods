def main():
    start = -1
    end = 1
    epsilon = pow(10, -6)

    start_point = start
    end_point = end
    iterations = 0
    while abs(end_point - start_point) > (2 * epsilon):
        iterations += 1
        middle_point = (start_point + end_point) / 2
        left_result = pow(start_point, 3) + 6 * pow(start_point, 2) + 9 * start_point + 1
        middle_result = pow(middle_point, 3) + 6 * pow(middle_point, 2) + 9 * middle_point + 1
        if left_result * middle_result < 0:
            end_point = middle_point
        else:
            start_point = middle_point
    result = (start_point + end_point) / 2
    print("Bisection method completed. Result is {} (iterations: {})".format(result, iterations))

    iterations = 0
    root = end
    old_root = end - 1
    while abs(root - old_root) > 2 * epsilon:
        iterations += 1
        old_root = root
        root = root - (1 / 24) * (pow(root, 3) + 6 * pow(root, 2) + 9 * root + 1)
    result = (root + old_root) / 2
    print("Iterative method completed. Result is {} (iterations: {})".format(result, iterations))

    iterations = 0
    root = end
    old_root = end - 1
    while abs(root - old_root) > 2 * epsilon:
        iterations += 1
        old_root = root
        root_function_value = pow(root, 3) + 6 * pow(root, 2) + 9 * root + 1
        next_root = root + root_function_value
        next_root_function_value = pow(next_root, 3) + 6 * pow(next_root, 2) + 9 * next_root + 1
        root = root - (root_function_value / (next_root_function_value - root_function_value)) * root_function_value
    result = (root + old_root) / 2
    print("Steffensen's method completed. Result is {} (iterations: {})".format(result, iterations))


main()
