import copy


def main():
    det = 1
    array = [[8.3, 3.1, 4.1, 1.9],
             [3.92, 8.45, 7.3, 2.46],
             [3.77, 7.69, 8.04, 2.28],
             [2.21, 3.17, 1.69, 6.69]]
    size = len(array)
    v_array = copy.deepcopy(array)
    c_array = copy.deepcopy(array)

    for k in range(0, size):
        max_element = abs(v_array[k][k])
        h = k
        w = k
        for l in range(k, size):
            for f in range(k, size):
                if max_element < abs(v_array[l][f]):
                    max_element = abs(v_array[l][f])
                    h = l
                    w = f

        for d in range(0, size):
            swap(v_array[k][d], v_array[h][d])

        for d in range(0, size):
            if d < k:
                swap(c_array[d][k], c_array[d][w])
            else:
                swap(v_array[d][k], v_array[d][w])

        det = det * pow(-1, w + h) * v_array[k][k]

        for i in range(k + 1, size):
            for j in range(k + 1, size):
                c_array[k][j] = v_array[k][j] / v_array[k][k]
                v_array[i][j] = v_array[i][j] - v_array[i][k] * c_array[k][j]

    print("Matrix:")
    print_matrix(array)
    print()

    print("Determinant of matrix is", det)


def swap(a, b):
    value = a
    a = b
    b = value


def print_matrix(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], "", end="")
        print()


main()

input("\n\nPress the Enter key to exit...")
