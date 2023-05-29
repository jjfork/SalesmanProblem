import random


def table_generator(number_of_cities, min_d, max_d):
    """
    Generates a table for Traveling Salesman Problem algorithm

    :param:
        number_of_cities: -> int, number of cities
        min_d: minimum distance between cities
        max_d: maximum distance between cities
    :return: table as a list of list

    - Distances between cities are random
    - Distances are symmetric, [i][j] = [j][i]
    """
    table = []
    for i in range(number_of_cities):
        value = []
        for j in range(number_of_cities):
            if i == j:
                value.append(0)
            elif j > i:
                value.append(random.randint(min_d, max_d))
            else:
                value.append(table[j][i])
        table.append(value)
    return table
