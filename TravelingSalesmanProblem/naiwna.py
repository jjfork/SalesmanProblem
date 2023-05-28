import sys
import itertools


def get_vertex_to_visit(graph: list, start_vertex: int) -> list:
    vertex_to_visit = []
    for vertex_index in range(len(graph)):
        if vertex_index != start_vertex:
            vertex_to_visit.append(vertex_index)
    return vertex_to_visit


def travelling_salesman_problem(graph: list, start_vertex: int) -> int:
    vertex_to_visit = get_vertex_to_visit(graph, start_vertex)

    min_path = sys.maxsize
    available_permutations = itertools.permutations(vertex_to_visit)

    for permutation in available_permutations:
        current_path_weight = 0
        current_vertex = start_vertex
        for vertex in permutation:
            current_path_weight += graph[current_vertex][vertex]
            current_vertex = vertex
        current_path_weight += graph[current_vertex][start_vertex]
        min_path = min(min_path, current_path_weight)

    return min_path
