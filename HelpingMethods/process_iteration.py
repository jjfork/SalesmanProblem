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