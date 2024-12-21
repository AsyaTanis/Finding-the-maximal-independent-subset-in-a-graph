import numpy as np
import random


def generate_random_edges(num_vertices: int, connection_percentage: float = 50) -> list:
    """
    Генерирует случайные рёбра для неориентированного графа на основе заданного процента связанных вершин.

    :param num_vertices: Количество вершин в графе.
    :param connection_percentage: Процент связанных вершин (от 0 до 100).
    :return: Список рёбер [(u, v), ...]
    """

    if not (0 <= connection_percentage <= 100):
        raise ValueError("connection_percentage должно быть в диапазоне от 0 до 100.")

    # Рассчитываем необходимое количество рёбер на основе процента
    max_possible_edges = num_vertices * (num_vertices - 1) // 2
    num_edges = int((connection_percentage / 100) * max_possible_edges)

    # Все возможные пары вершин (без повторов, т.к. граф неориентированный)
    possible_edges = [(u, v) for u in range(num_vertices) for v in range(u + 1, num_vertices)]

    # Случайно выбираем необходимое количество рёбер
    edges = random.sample(possible_edges, num_edges)

    edges.sort()
    return edges


def edges_to_adjacency_matrix(edges):
    """
    Преобразует список рёбер неориентированного графа в матрицу смежности.

    :param edges: список рёбер графа в виде упорядоченных пар [(u, v), (x, y), ...]
    :return: квадратная матрица смежности numpy.ndarray
    """
    if not edges:
        return np.array([[]])  # Пустая матрица, если нет рёбер

    # Определяем максимальный номер вершины
    max_vertex = max(max(u, v) for u, v in edges)

    # Инициализируем матрицу смежности
    adjacency_matrix = np.zeros((max_vertex + 1, max_vertex + 1), dtype=int)

    # Заполняем матрицу смежности
    for u, v in edges:
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1  # Так как граф неориентированный

    return adjacency_matrix

# def print_matrix(matrix):
#     for row in matrix:
#         print("[" + ", ".join(map(str, row)) + "],")
#
#
# if __name__ == "__main__":
#     # Получаем размер матрицы
#     size = int(input("Введите размер матрицы: "))
#
#     # Генерируем симметричную матрицу смежности
#     edges = generate_random_edges(size)
#     matrix = edges_to_adjacency_matrix(edges)
#
