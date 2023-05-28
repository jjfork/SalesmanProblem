import itertools
import random
import sys


def held_karp(graph: list) -> int:
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
    bits = 0
    for bit in subset:
        bits |= 1 << bit
    return bits


def resolve_path(bits, parent, path, vertex_count, vertex_set):
    for i in range(vertex_count - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = vertex_set[(bits, parent)]
        bits = new_bits
    path.append(0)


def get_min_path(graph, vertex_count, vertex_set):
    bits = (2**vertex_count - 1) - 1
    res = []
    for vertex_index in range(1, vertex_count):
        res.append((vertex_set[(bits, vertex_index)][0] + graph[vertex_index][0], vertex_index))
    return bits, res


def get_min_distance_in_subset(graph, prev, subset, vertex_index, vertex_set):
    result = []
    for current_vertex_index in subset:
        if current_vertex_index == 0 or current_vertex_index == vertex_index:
            continue
        distance = vertex_set[(prev, current_vertex_index)][0] + graph[current_vertex_index][vertex_index]
        result.append((distance, current_vertex_index))
    return min(result)


def get_vertexes_set(graph, vertex_count) -> dict:
    vertex_map = {}
    for vertex_index in range(vertex_count):
        if vertex_index != 0:
            vertex_map[(1 << vertex_index, vertex_index)] = (graph[0][vertex_index], 0)
    return vertex_map
