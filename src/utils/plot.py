import matplotlib.pyplot as plt
from src.utils.generator import generate_random_edges, edges_to_adjacency_matrix
from src.core.mult import find_maximal_independent_sets_parallel
from src.core.posled import find_maximal_independent_sets_posled
import time
from typing import List, Tuple


def benchmark_independent_set_algorithms(vertex_array: List[int]) -> Tuple[List[float], List[float]]:

    sequential_times = []
    parallel_times = []

    for num_vertices in vertex_array:

        edges = generate_random_edges(num_vertices)
        adjacency_matrix = edges_to_adjacency_matrix(edges)

        start_time = time.time()
        find_maximal_independent_sets_posled(adjacency_matrix)
        end_time = time.time()
        sequential_times.append(end_time - start_time)


        start_time = time.time()
        find_maximal_independent_sets_parallel(adjacency_matrix)
        end_time = time.time()
        parallel_times.append(end_time - start_time)

    return sequential_times, parallel_times


if __name__ == '__main__':

    vertex_counts = [10, 50, 100, 200, 300, 400, 500, 800, 1000, 1500]
    sequential_times = [0.001, 0.009, 0.04, 0.13, 0.42, 1.1, 2.4, 11.74, 21.32, 87.68]
    parallel_times_4 = [0.5, 0.55, 0.52, 0.7, 0.87, 1.12, 1.76, 6.28, 9.72, 36.24]
    parallel_times_8 = [0.48, 0.5, 0.5, 0.6, 0.75, 1.06, 1.73, 5.60, 10.06, 31.36]
    plt.figure(figsize=(10, 6))
    plt.plot(vertex_counts, sequential_times, label="Последовательный", marker='o')
    plt.plot(vertex_counts, parallel_times_8, label="Параллельный для 8 процессов", marker='s')
    plt.plot(vertex_counts, parallel_times_4, label="Параллельный для 4 процессов", marker='s')
    plt.xlabel("Количество вершин графа")
    plt.ylabel("Время (в сек)")
    plt.title("Зависимость времени выполнения алгоритма Брона-Кербоша от количества вершин")
    plt.xticks(range(0, 1600, 100))
    plt.yticks(range(0, 100, 10))
    plt.legend()
    plt.grid()
    plt.show()



    # vertex_counts = [10, 50, 100, 200, 300, 400, 500, 800, 1000]
    # sequential_times = [0.001, 0.009, 0.04, 0.13, 0.42, 1.1, 2.4, 9.35, 17.67]
    # parallel_times = [0.5, 0.5, 0.5, 0.6, 0.75, 1.06, 1.73, 5.5, 9.78]
    # plt.figure(figsize=(10, 6))
    # plt.plot(vertex_counts, sequential_times, label="Последовательный", marker='o')
    # plt.plot(vertex_counts, parallel_times, label="Параллельный", marker='s')
    # plt.xlabel("Количество вершин графа")
    # plt.ylabel("Время (в сек)")
    # plt.title("Зависимость количества вершин от времени выполнения алгоритма Брона-Кербоша")
    # plt.legend()
    # plt.grid()
    # plt.show()
