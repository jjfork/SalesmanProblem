import itertools


def held_karp(graph: list) -> int:
    """
    Traveling Salesman Problem using Held-Karp algorithm
    :param:
        graph: -> list, input graph as a list

    :return: -> int, minimum distance of optimal tour
    """
    vertex_count = len(graph)
    vertex_set = get_vertexes_set(graph, vertex_count)

    for subset_size in range(2, vertex_count):
        for subset in itertools.combinations(range(1, vertex_count), subset_size):

            bits = sum_bits_for_all_index(subset)

            for vertex_index in subset:
                prev_subset_index = bits & ~(1 << vertex_index)

                vertex_set[(bits, vertex_index)] = get_min_distance_in_subset(graph,
                                                                              prev_subset_index,
                                                                              subset,
                                                                              vertex_index,
                                                                              vertex_set)

    # last subset bits
    bits, res = get_min_path(graph, vertex_count, vertex_set)
    min_distance, parent = min(res)

    # Backtrack to find full path
    path = []
    resolve_path(bits, parent, path, vertex_count, vertex_set)

    return min_distance, list(reversed(path))


def sum_bits_for_all_index(subset):
    """
    Calculate sum of bits for all indices in given subset
    :param:
        subset:  subset of indices
    :return: -> int, sum of bits
    """
    bits = 0
    for bit in subset:
        bits |= 1 << bit
    return bits


def resolve_path(bits, parent, path, vertex_count, vertex_set):
    """
    Backtrack to find optimal patch basen on bits, parent and vertex_set information
    :param:
        bits: representation of visited cities
        parent: parent vertex
        path: list to store optimal path
        vertex_count: int, number of vertices in graph
        vertex_set: vertex set containing distance info
    """
    for i in range(vertex_count - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = vertex_set[(bits, parent)]
        bits = new_bits
    path.append(0)


def get_min_path(graph, vertex_count, vertex_set):
    """
    Find minimum path for last subset
    :param:
        graph: -> list, input graph as a list
        vertex_count: -> int, number of vertices in graph
        vertex_set: -> dict, vertex set containing distance info

    :return: -> tuple, a bit representation of visited cities and list of tuples with min distances and vertex index
    """
    bits = (2**vertex_count - 1) - 1
    res = []
    for vertex_index in range(1, vertex_count):
        res.append((vertex_set[(bits, vertex_index)][0] + graph[vertex_index][0], vertex_index))
    return bits, res


def get_min_distance_in_subset(graph, prev, subset, vertex_index, vertex_set):
    """
        Find minimum path for given subset of cities
        :param:
            graph: -> list, input graph as a list
            prev: -> int, previous subset
            subset: -> tuple, current subset of cities
            vertex_index: -> int, current vertex index
            vertex_set: -> dict, vertex set containing distance info

        :return: -> tuple, vertex set with distance info
        """
    result = []
    for current_vertex_index in subset:
        if current_vertex_index == 0 or current_vertex_index == vertex_index:
            continue
        distance = vertex_set[(prev, current_vertex_index)][0] + graph[current_vertex_index][vertex_index]
        result.append((distance, current_vertex_index))
    return min(result)


def get_vertexes_set(graph, vertex_count) -> dict:
    """
    Generate initial vertex map, stores distances between start vertex and all other
    Assuming starting vertex is always at index 0 in graph
    :param
        graph: -> list, input graph as a list
        vertex_count: -> int, number of vertices in graph
    :return: dict, map of vertices to their distances
    """
    vertex_map = {}
    for vertex_index in range(vertex_count):
        if vertex_index != 0:
            vertex_map[(1 << vertex_index, vertex_index)] = (graph[0][vertex_index], 0)
    return vertex_map
