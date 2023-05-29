from SalesmanProblem.HelpingMethods.table_generator import table_generator
from SalesmanProblem.TravelingSalesmanProblem.helda_karpa import held_karp
from SalesmanProblem.TravelingSalesmanProblem.naiwna import travelling_salesman_problem

if __name__ == "__main__":
    starting_point = 0
    example_data = table_generator(10, 1, 9)

    print("rozwiązanie naiwne:")
    print(travelling_salesman_problem(example_data, starting_point))

    print("Helda-Karpa:")
    print(held_karp(example_data)[0])

    print("najbliższego sąsiada:")

    print("najmniejszej krawędzi:")


