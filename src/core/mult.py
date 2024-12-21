from multiprocessing import Pool
from typing import List, Tuple
import time
from concurrent.futures import ThreadPoolExecutor

def bron_kerbosch(graph, index):
    aproved = [index]
    worked = graph[index]

    while worked:
        new_worked = set()

        for i in worked:
            if i not in aproved:
                add = True
                for j in aproved:
                    if i not in graph[j]:
                        add = False
                        break
                if add:
                    aproved.append(i)
                    new_worked |= set(graph[i])
        worked = list(new_worked.copy())
    return aproved


def find_maximal_independent(graph):
    independent_sets = []

    # Используем Pool для распараллеливания
    with Pool() as p:
        results = p.starmap(bron_kerbosch, [(graph, i) for i in range(len(graph))])
    for res in results:
        res_sorted = sorted(res)
        if res_sorted not in independent_sets:
            independent_sets.append(res_sorted)

    max_length = max(len(independent_set) for independent_set in list(independent_sets))
    max_length_sets = [independent_set for independent_set in independent_sets if len(independent_set) == max_length]

    print("Максимальное независимое множество:")
    for independent_set in max_length_sets:
        print(sorted(independent_set))


# def find_unconnected_vertices(matrix):
#     unconnected_vertices = []
#     for i in range(len(matrix)):
#         unconnected = set()
#
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 0 and i != j:
#                 unconnected.add(j)
#
#         unconnected_vertices.append(sorted(unconnected))
#
#     return unconnected_vertices

def find_unconnected_for_vertex(i, matrix):
    unconnected = set()
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0 and i != j:
            unconnected.add(j)
    return sorted(unconnected)


def find_unconnected_vertices(matrix):
    unconnected_vertices = []

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda i: find_unconnected_for_vertex(i, matrix), range(len(matrix))))

    return results

def find_maximal_independent_sets_parallel(graph):
    result = find_unconnected_vertices(graph)
    find_maximal_independent(result)


# def edges_to_adjacency_matrix(edges: List[Tuple[int, int]]) -> List[List[int]]:
#     max_node = max(max(u, v) for u, v in edges)
#     n = max_node + 1
#
#     adjacency_matrix: List[List[int]] = [[0] * n for _ in range(n)]
#
#     for u, v in edges:
#         adjacency_matrix[u][v] = 1
#         adjacency_matrix[v][u] = 1
#
#     return adjacency_matrix


#
# if __name__ == "__main__":
#
#     adjacency_matrix = edges_to_adjacency_matrix(e_10000)
#
#     print("Выполнение параллельной части программы")
#
#     start_time_parallel = time.time()
#     find_maximal_independent_sets_parallel(adjacency_matrix)
#     end_time_parallel = time.time()
#
#     delta_parallel = end_time_parallel - start_time_parallel
#     print("Время: ", delta_parallel)