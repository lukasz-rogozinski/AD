import csv
import iris


def read_data_from_file():
    iris_objects = []
    with open('iris.data') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        for row in data:
            iris_objects.append(iris.Iris(float(row[0]), float(row[1]), float(row[2]), float(row[3]), row[4]))

    return iris_objects


def print_matrix_results(results):
    row_format = "{:>15}" * len(results[0])
    for row in results:
        print(row_format.format(*row))
    print('\n')
