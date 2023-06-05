def krawedzi(graph: list):
    table = generate_table_asc_paths(graph)
    access = access_to_node(len(graph))
    path = 0
    node_added = 0

    for record in table:
        left_node = access[record[0]][0]
        right_node = access[record[1]][0]
        left_node_edges = access[record[0]][1]
        right_node_edges = access[record[1]][1]

        distance = record[2]
        algotihm_condition = left_node.isdisjoint(right_node) and left_node_edges < 2 and right_node_edges < 2

        if algotihm_condition or node_added == len(graph) - 1:
            path += distance
            node_added += 1
            access[record[0]][1] += 1
            access[record[1]][1] += 1
            tmp = left_node.union(right_node)
            for ele in tmp:
                access[ele][0] = tmp
    if node_added != len(graph):
        return None

    return path


def generate_table_asc_paths(graph: list):
    paths = []
    node_count = len(graph)
    for row in range(node_count - 1):
        for col in range(row + 1, node_count):
            element = (row, col, graph[row][col])
            paths.append(element)
    paths.sort(key=lambda x: x[2])
    return paths


def access_to_node(node_count: int):
    map_node = {}
    for node_index in range(node_count):
        new_set = set()
        new_set.add(node_index)
        map_node[node_index] = [new_set, 0]
    return map_node
