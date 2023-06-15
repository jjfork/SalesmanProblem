import multiprocessing
import time

from SalesmanProblem.HelpingMethods.table_generator import table_generator
from SalesmanProblem.TravelingSalesmanProblem.naiwna import TSP_bruteForce


def process_iteration(size, starting_point):
    array = table_generator(number_of_cities=size, min_d=1, max_d=9)
    start = time.perf_counter_ns()
    result = TSP_bruteForce(array, starting_point)
    finish = time.perf_counter_ns()
    t = (finish - start) / 1_000_000_000
    return t


if __name__ == '__main__':
    monte_carlo = 1
    cities_size = [5, 10, 12]  # example list of cities sizes
    starting_point = 0  # example starting point

    result_naive = []
    print('Naive Solution')

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())  # use maximum available CPU cores

    for i in range(monte_carlo):
        results = pool.starmap(process_iteration, [(size, starting_point) for size in cities_size])
        result_naive.append(results)
        print('^^^Performed', i + 1, 'check^^^')

    pool.close()
    pool.join()
    print(result_naive)


    # Naive Solution
    # print('Naive Solution')
    # for i in range(monte_carlo):
    #     result = []
    #     for size in cities_size:
    #         array = table_generator(number_of_cities=size, min_d=1, max_d=9)
    #
    #         start = time.perf_counter_ns()
    #         print(travelling_salesman_problem(array, starting_point))
    #         finish = time.perf_counter_ns()
    #
    #         t = (finish - start) / 1_000_000_000
    #         result.append(t)
    #
    #     result_naive.append(result)
    #     print('^^^Performed ', i + 1, ' check ^^^')