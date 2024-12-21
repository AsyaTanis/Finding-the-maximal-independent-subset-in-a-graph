from src.utils.generator import generate_random_edges
from src.core.mult import find_maximal_independent_sets_parallel
from src.core.posled import find_maximal_independent_sets_posled
import time
from typing import List, Tuple

def edges_to_adjacency_matrix(edges: List[Tuple[int, int]]) -> List[List[int]]:
    max_node = max(max(u, v) for u, v in edges)
    n = max_node + 1

    adjacency_matrix: List[List[int]] = [[0] * n for _ in range(n)]

    for u, v in edges:
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1

    return adjacency_matrix


def save_edges_to_file(edges, filename):
    with open(filename, 'w') as file:
        for edge in edges:
            file.write(f"{edge}, ")


if __name__ == "__main__":
    num_vertices = int(input("Введите количество вершин: "))
    edges = generate_random_edges(num_vertices)
    save_edges_to_file(edges, f'edges_generate_{num_vertices}.py')
    adjacency_matrix = edges_to_adjacency_matrix(edges)
    print("Выполнение последовательной части программы")

    start_time = time.time()
    find_maximal_independent_sets_posled(adjacency_matrix)
    end_time = time.time()

    delta_posled = end_time - start_time
    print("Время: ", delta_posled)

    print("Выполнение параллельной части программы")

    start_time_parallel = time.time()
    find_maximal_independent_sets_parallel(adjacency_matrix)
    end_time_parallel = time.time()

    delta_parallel = end_time_parallel - start_time_parallel
    print("Время: ", delta_parallel)
