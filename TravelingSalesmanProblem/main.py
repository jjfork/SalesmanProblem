from SalesmanProblem.TravelingSalesmanProblem.helda_karpa import held_karp
from SalesmanProblem.TravelingSalesmanProblem.naiwna import travelling_salesman_problem

if __name__ == "__main__":
    starting_point = 0
    example_data = [
        [0, 7, 4, 8, 3, 2, 9, 5, 6, 1],
        [7, 0, 6, 9, 5, 3, 8, 4, 2, 7],
        [4, 6, 0, 3, 7, 9, 2, 8, 5, 4],
        [8, 9, 3, 0, 4, 6, 5, 7, 9, 8],
        [3, 5, 7, 4, 0, 1, 3, 6, 8, 2],
        [2, 3, 9, 6, 1, 0, 5, 4, 7, 3],
        [9, 8, 2, 5, 3, 5, 0, 3, 4, 9],
        [5, 4, 8, 7, 6, 4, 3, 0, 1, 6],
        [6, 2, 5, 9, 8, 7, 4, 1, 0, 5],
        [1, 7, 4, 8, 2, 3, 9, 6, 5, 0]]

    print("rozwiązanie naiwne:")
    print(travelling_salesman_problem(example_data, starting_point))

    print("Helda-Karpa:")
    print(held_karp(example_data, starting_point))

    print("najbliższego sąsiada:")

    print("najmniejszej krawędzi:")


