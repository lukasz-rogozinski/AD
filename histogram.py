import numpy
import matplotlib.pyplot as pyp


def calculate_histogram(correlation, iris):
    data = [list(map(lambda i: i.sepal_width, iris)), list(map(lambda i: i.sepal_length, iris)),
            list(map(lambda i: i.petal_width, iris)), list(map(lambda i: i.petal_length, iris))]
    maximum = (1, 2)
    for i in range(1, 5):
        for j in range(i + 1, 5):
            if abs(correlation[i][j]) > abs(correlation[maximum[0]][maximum[1]]):
                maximum = (i, j)

    histogram_x = numpy.histogram(data[maximum[0] - 1])
    histogram_y = numpy.histogram(data[maximum[1] - 1])

    return [(correlation[maximum[0]][0], histogram_x), (correlation[0][maximum[1]], histogram_y)]


def print_histogram(title, histogram):
    pyp.bar(list(map(lambda h: str(round(h, 2)), histogram[1][:-1])), histogram[0])
    pyp.suptitle(title)
    pyp.show()


def execute(correlation, flowers):
    result = calculate_histogram(correlation, flowers)
    print_histogram(result[0][0], result[0][1])
    print_histogram(result[1][0], result[1][1])
