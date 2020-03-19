import statistics
import common


def calculate_median_min_max(flowers):
    result = [('Name:', 'Median:', 'Minimum:', 'Maximum'),
              calculate_results(map(lambda f: f.sepal_length, flowers), 'Sepal length:'),
              calculate_results(map(lambda f: f.sepal_width, flowers), 'Sepal width:'),
              calculate_results(map(lambda f: f.petal_length, flowers), 'Petal length:'),
              calculate_results(map(lambda f: f.petal_width, flowers), 'Petal width:')]

    return result


def calculate_results(values, name):
    list_of_values = list(values)
    median = statistics.median(list_of_values)
    minimum = min(list_of_values)
    maximum = max(list_of_values)
    return name, median, minimum, maximum


def execute(flowers):
    common.print_matrix_results(calculate_median_min_max(flowers))
