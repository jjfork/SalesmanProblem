import sys
import itertools


def get_vertex_to_visit(graph: list, start_vertex: int) -> list:
    """
    Generate list of vertices to visit, excluding start vertex
    :param:
        graph: -> list, input graph as a list
        start_vertex: -> int, starting vertex
    :return: -> list, vertices to visit
    """
    vertex_to_visit = []
    for vertex_index in range(len(graph)):
        if vertex_index != start_vertex:
            vertex_to_visit.append(vertex_index)
    return vertex_to_visit


def TSP_bruteForce(graph: list, start_vertex: int) -> int:
    """
    Brute force approach to solve Traveling Salesman Problem (TSP)
    :param:
        graph: -> list, input graph as a list
        start_vertex: -> int, starting vertex
    :return: -> int, minimum path weight of tour
    """
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
