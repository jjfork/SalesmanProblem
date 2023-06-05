from SalesmanProblem.HelpingMethods.table_generator import table_generator
from SalesmanProblem.TravelingSalesmanProblem.helda_karpa import held_karp
from SalesmanProblem.TravelingSalesmanProblem.naiwna import travelling_salesman_problem
from SalesmanProblem.TravelingSalesmanProblem.najblizszego_sąsiada import closest_neigh
from SalesmanProblem.TravelingSalesmanProblem.najmniejszej_krawędzi import krawedzi

if __name__ == "__main__":
    starting_point = 0
    example_data = table_generator(number_of_cities=5, min_d=1, max_d=9)
    example_data = [
        [0, 8, 5, 7, 1],
        [8, 0, 7, 8, 6],
        [5, 7, 0, 3, 8],
        [7, 8, 3, 0, 1],
        [1, 6, 8, 1, 0],
    ]
    for row in example_data:
        print(row)
    print("rozwiązanie naiwne:")
    print(travelling_salesman_problem(example_data, starting_point))

    print("Helda-Karpa:")
    print(held_karp(example_data)[0])

    print("najbliższego sąsiada:")
    print(closest_neigh(example_data, starting_point))
    print("najmniejszej krawędzi:")
    print(krawedzi(example_data))


