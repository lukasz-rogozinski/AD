import numpy
import common


def calculate_correlation(flowers):
    data = [list(map(lambda f: f.sepal_width, flowers)), list(map(lambda f: f.sepal_length, flowers)),
            list(map(lambda f: f.petal_width, flowers)), list(map(lambda f: f.petal_length, flowers))]
    result = [
        ['Name:', 'Sepal width', 'Sepal length', 'Petal width:', 'Petal length'],
        ['Sepal width', 0, 0, 0, 0],
        ['Sepal length', 0, 0, 0, 0],
        ['Petal width', 0, 0, 0, 0],
        ['Petal length', 0, 0, 0, 0]
    ]

    for i in range(4):
        for j in range(4):
            result[i + 1][j + 1] = round(numpy.corrcoef(data[i], data[j])[0][1], 4)
    # wspolczynnik korelacji liniowe Pearsona
    return result


def execute(flowers):
    result = calculate_correlation(flowers)
    common.print_matrix_results(result)
    return result
