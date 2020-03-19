import collections


def calculate_dominant(all_flower_types):
    distinct_flower_types = list(collections.OrderedDict.fromkeys(all_flower_types))
    number_of_each_flower_types = list(
        map(lambda flower_type: (flower_type, count_values(flower_type, all_flower_types)), distinct_flower_types))
    max_value = max(map(lambda flower_type_tuple: flower_type_tuple[1], number_of_each_flower_types))
    return list(filter(lambda flower_type_tuple: flower_type_tuple[1] == max_value, number_of_each_flower_types))


def count_values(flower_type, all_flower_types):
    return len(list(filter(lambda value: value == flower_type, all_flower_types)))


def print_dominant(flower_type_tuples):
    if len(flower_type_tuples) > 1:
        print('Multiple values have the same value. Can not determine dominant:')
    for tuple in flower_type_tuples:
        print(f'{tuple[0]} - {tuple[1]}')
    print('\n')


def execute(all_flower_types):
    result = calculate_dominant(all_flower_types)
    print_dominant(result)
