from SalesmanProblem.HelpingMethods.table_generator import table_generator
from SalesmanProblem.TravelingSalesmanProblem.helda_karpa import held_karp
from SalesmanProblem.TravelingSalesmanProblem.naiwna import travelling_salesman_problem
from SalesmanProblem.TravelingSalesmanProblem.najblizszego_sąsiada import closest_neigh
from SalesmanProblem.TravelingSalesmanProblem.najmniejszej_krawędzi import min_span_tree

# imports use in counting times and creating graphs
from matplotlib import pyplot as plt
import time

if __name__ == "__main__":
    starting_point = 0
    monte_carlo = 10
    cities_size = [10, 15, 20]

    # creating lists to which the results will be saved
    result_naive = []
    result_held_karp = []
    result_closest_neigh = []
    result_min_span_tree = []

    # Held-Karp Algorithm
    print('Held-Karp Algorithm')
    for i in range(1):
        result = []
        for size in cities_size:
            array = table_generator(number_of_cities=size, min_d=1, max_d=9)

            start = time.perf_counter_ns()
            print(held_karp(array)[0])
            finish = time.perf_counter_ns()

            t = (finish - start) / 1_000_000_000
            result.append(t)

        result_held_karp.append(result)
        print('Performed ', i + 1, ' check')

    # Closest Neighbour Algorithm
    print('Closest Neighbour Algorithm')
    for i in range(monte_carlo):
        result = []
        for size in cities_size:
            array = table_generator(number_of_cities=size, min_d=1, max_d=9)

            start = time.perf_counter_ns()
            print(closest_neigh(array, starting_point))
            finish = time.perf_counter_ns()

            t = (finish - start) / 1_000_000
            result.append(t)

        result_closest_neigh.append(result)
        print('Performed ', i + 1, ' check')

    # Minimum Spanning Tree Algorithm
    print('Minimum Spanning Tree Algorithm')
    for i in range(monte_carlo):
        result = []
        for size in cities_size:
            array = table_generator(number_of_cities=size, min_d=1, max_d=9)

            start = time.perf_counter_ns()
            print(min_span_tree(array))
            finish = time.perf_counter_ns()

            t = (finish - start) / 1_000_000
            result.append(t)

        result_min_span_tree.append(result)
        print('Performed ', i + 1, ' check')

     # Naive Solution
     print('Naive Solution')
     for i in range(monte_carlo):
         result = []
         for size in cities_size:
             array = table_generator(number_of_cities=size, min_d=1, max_d=9)
    
             start = time.perf_counter_ns()
             print(travelling_salesman_problem(array, starting_point))
             finish = time.perf_counter_ns()
    
             t = (finish - start) / 1_000_000_000
             result.append(t)
    
         result_naive.append(result)
         print('Performed ', i+1, ' check')

    # printing all results
    print(result_naive)
    print(result_held_karp)
    print(result_closest_neigh)
    print(result_min_span_tree)

     # creating graphs for each algorithm - Naive
     plt.subplot(2, 2, 1)
    
    # counting average of results and plotting - only for display of legend
     averages = [sum(column) / len(column) for column in zip(*result_naive)]
     plt.plot(cities_size, averages, color='#FF0000')
    
     for results in result_naive:
         plt.plot(cities_size, results, color='#E39DE3')
    
     # plotting average to be on top of other graphs
     plt.plot(cities_size, averages, color='#FF0000')
    
     # editing plot
     plt.title('Naive Solution')
     plt.xlabel('Number of cities')
     plt.ylabel('Time (s)')
     plt.legend(['Average of results', 'Monte Carlo results'], loc='upper left')

    # creating graphs for each algorithm - Held-Karp
    plt.subplot(2, 2, 2)

    # counting average of results and plotting - only for display of legend
    averages = [sum(column) / len(column) for column in zip(*result_held_karp)]
    plt.plot(cities_size, averages, color='#FF0000')

    for results in result_held_karp:
        plt.plot(cities_size, results, color='#E39DE3')

    # plotting average to be on top of other graphs
    plt.plot(cities_size, averages, color='#FF0000')

    # editing plot
    plt.title('Held-Karp Algorithm')
    plt.xlabel('Number of cities')
    plt.ylabel('Time (s)')
    plt.legend(['Average of results', 'Monte Carlo results'], loc='upper left')

    # creating graphs for each algorithm - Closest Neighbour
    plt.subplot(2, 2, 3)

    # counting average of results and plotting - only for display of legend
    averages = [sum(column) / len(column) for column in zip(*result_closest_neigh)]
    plt.plot(cities_size, averages, color='#FF0000')

    for results in result_closest_neigh:
        plt.plot(cities_size, results, color='#E39DE3')

    # plotting average to be on top of other graphs
    plt.plot(cities_size, averages, color='#FF0000')

    # editing plot
    plt.title('Nearest Neighbour Algorithm')
    plt.xlabel('Number of cities')
    plt.ylabel('Time (ms)')
    plt.legend(['Average of results', 'Monte Carlo results'], loc='upper left')

    # creating graphs for each algorithm - Minimum Spanning Tree
    plt.subplot(2, 2, 4)

    # counting average of results and plotting - only for display of legend
    averages = [sum(column) / len(column) for column in zip(*result_min_span_tree)]
    plt.plot(cities_size, averages, color='#FF0000')

    for results in result_min_span_tree:
        plt.plot(cities_size, results, color='#E39DE3')

    # plotting average to be on top of other graphs
    plt.plot(cities_size, averages, color='#FF0000')

    # editing plot
    plt.title('Minimum Spanning Tree Algorithm')
    plt.xlabel('Number of cities')
    plt.ylabel('Time (ms)')
    plt.legend(['Average of results', 'Monte Carlo results'], loc='upper left')

    # showing graphs
    plt.show()
