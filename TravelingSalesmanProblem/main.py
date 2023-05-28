from SalesmanProblem.TravelingSalesmanProblem.helda_karpa import held_karp
from SalesmanProblem.TravelingSalesmanProblem.naiwna import travelling_salesman_problem

if __name__ == "__main__":
    starting_point = 0
    example_data = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 40, 45],
    [15, 35, 0, 30, 20],
    [20, 40, 30, 0, 10],
    [25, 45, 20, 10, 0]
]

    print("rozwiązanie naiwne:")
    print(travelling_salesman_problem(example_data, starting_point))

    print("Helda-Karpa:")
    print(held_karp(example_data)[0])

    print("najbliższego sąsiada:")

    print("najmniejszej krawędzi:")


