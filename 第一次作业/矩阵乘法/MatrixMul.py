import sys


def matrixmul(a, b):
    if len(a) != len(b[0]):
        return False
    else:
        result = [[0] * len(b[0]) for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result


def main(argv):
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    print(matrixmul(a, b))
    pass


if __name__ == "__main__":
    main(sys.argv)

