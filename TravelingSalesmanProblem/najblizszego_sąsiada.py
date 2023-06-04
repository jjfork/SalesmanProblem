import sys


def closest_neigh(graph: list, start_vertex: int) -> int:
    visited_indexes = [start_vertex]
    actual_vertex = start_vertex
    min_path = 0
    for cokolwiek in range(len(graph) - 1):
        operation_list = graph[actual_vertex].copy()
        replace_visited_indexes(operation_list, visited_indexes)
        closest_neighbor_path = min(operation_list)
        min_path += closest_neighbor_path
        closest_neighbor = operation_list.index(closest_neighbor_path)
        visited_indexes.append(closest_neighbor)
        actual_vertex = closest_neighbor
    min_path += graph[start_vertex][actual_vertex]

    return min_path


def replace_visited_indexes(operation_list, visited_indexes):
    for index in visited_indexes:
        operation_list[index] = sys.maxsize





