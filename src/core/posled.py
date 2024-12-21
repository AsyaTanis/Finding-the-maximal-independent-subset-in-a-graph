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
    for i in range(len(graph)):
        res = sorted(bron_kerbosch(graph, i))
        if res not in independent_sets:
            independent_sets.append(res)
    max_length = max(len(independent_set) for independent_set in list(independent_sets))
    max_length_sets = [independent_set for independent_set in independent_sets if len(independent_set) == max_length]
    print("Максимальное независимое множество:")
    for independent_set in max_length_sets:
        print(sorted(independent_set))


def find_unconnected_vertices(matrix):
    unconnected_vertices = []
    for i in range(len(matrix)):
        unconnected = set()
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0 and i != j:
                unconnected.add(j)
        unconnected_vertices.append(sorted(unconnected))
    return unconnected_vertices


def find_maximal_independent_sets_posled(graph):
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
#     num_vertices = int(input("Введите количество вершин: "))
#     edges = generate_random_edges(num_vertices)
#     adjacency_matrix = edges_to_adjacency_matrix(edges)
#     print(adjacency_matrix)
#     print("Выполнение последовательной части программы")
#
#     start_time = time.time()
#     find_maximal_independent_sets_posled(adjacency_matrix)
#     end_time = time.time()
#
#     delta_posled = end_time - start_time
#     print("Время: ", delta_posled)