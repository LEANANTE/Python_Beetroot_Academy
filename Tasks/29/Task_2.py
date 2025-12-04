"""
Task 2: Using breadth-first search write an algorithm that can determine 
the shortest path from each vertex to every other vertex.
This is called the all-pairs shortest path problem.

Для невзважених графів (або графів з однаковою вагою ребер):
- BFS знаходить найкоротший шлях від однієї вершини до всіх інших
- Для all-pairs shortest path - запускаємо BFS з кожної вершини

Часова складність: O(V * (V + E)) = O(V² + VE)
Просторова складність: O(V²) для зберігання всіх відстаней
"""

import sys
from typing import Dict, List, Optional, Tuple
from collections import deque


class Vertex:
    """Клас вершини графа"""

    def __init__(self, key):
        self._key = key
        self._neighbors: Dict["Vertex", int] = {}
        self._color = "white"
        self._distance = sys.maxsize
        self._previous: Optional["Vertex"] = None

    @property
    def key(self):
        return self._key

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, value):
        self._previous = value

    def add_neighbor(self, neighbor: "Vertex", weight: int = 0):
        self._neighbors[neighbor] = weight

    def get_neighbors(self):
        return self._neighbors.keys()

    def __str__(self):
        return f"Vertex({self._key})"

    def __repr__(self):
        return self.__str__()


class Graph:
    """Клас графа з підтримкою All-Pairs Shortest Path"""

    def __init__(self):
        self._vertices: Dict[str, Vertex] = {}

    def add_vertex(self, key) -> Vertex:
        """Додати вершину до графа"""
        if key not in self._vertices:
            self._vertices[key] = Vertex(key)
        return self._vertices[key]

    def get_vertex(self, key) -> Optional[Vertex]:
        """Отримати вершину за ключем"""
        return self._vertices.get(key, None)

    def add_edge(self, from_key, to_key, weight: int = 0, bidirectional: bool = False):
        """Додати ребро (можливо двонаправлене)"""
        if from_key not in self._vertices:
            self.add_vertex(from_key)
        if to_key not in self._vertices:
            self.add_vertex(to_key)
        self._vertices[from_key].add_neighbor(self._vertices[to_key], weight)
        if bidirectional:
            self._vertices[to_key].add_neighbor(self._vertices[from_key], weight)

    def get_vertices(self):
        """Отримати всі вершини"""
        return self._vertices.values()

    def get_vertex_keys(self):
        """Отримати всі ключі вершин"""
        return list(self._vertices.keys())

    def __iter__(self):
        return iter(self._vertices.values())

    def __contains__(self, key):
        return key in self._vertices

    def __len__(self):
        return len(self._vertices)

    def reset(self):
        """Скинути стан всіх вершин"""
        for vertex in self._vertices.values():
            vertex.color = "white"
            vertex.distance = sys.maxsize
            vertex.previous = None

    def bfs(self, start_key) -> Dict[str, int]:
        """
        Breadth-First Search від однієї вершини
        Повертає словник: {vertex_key: distance}
        """
        self.reset()
        distances = {}

        start = self.get_vertex(start_key)
        if start is None:
            return distances

        start.distance = 0
        start.color = "gray"
        queue = deque([start])

        while queue:
            current = queue.popleft()

            for neighbor in current.get_neighbors():
                if neighbor.color == "white":
                    neighbor.color = "gray"
                    neighbor.distance = current.distance + 1
                    neighbor.previous = current
                    queue.append(neighbor)

            current.color = "black"
            distances[current.key] = current.distance

        # Додати недосяжні вершини з нескінченною відстанню
        for key in self._vertices:
            if key not in distances:
                distances[key] = float('inf')

        return distances

    def all_pairs_shortest_path_bfs(self) -> Dict[str, Dict[str, int]]:
        """
        All-Pairs Shortest Path використовуючи BFS
        
        Повертає словник словників:
        {
            source1: {dest1: distance, dest2: distance, ...},
            source2: {dest1: distance, dest2: distance, ...},
            ...
        }
        
        Працює для невзважених графів або графів з однаковою вагою ребер
        """
        all_distances = {}

        for vertex_key in self._vertices:
            # Запускаємо BFS з кожної вершини
            all_distances[vertex_key] = self.bfs(vertex_key)

        return all_distances

    def get_shortest_path(self, start_key, end_key) -> Tuple[List[str], int]:
        """
        Отримати найкоротший шлях та його довжину між двома вершинами
        Повертає: (шлях як список ключів, довжина шляху)
        """
        self.bfs(start_key)

        end = self.get_vertex(end_key)
        if end is None or end.distance == sys.maxsize:
            return [], float('inf')

        # Відновити шлях
        path = []
        current = end
        while current is not None:
            path.append(current.key)
            current = current.previous

        path.reverse()
        return path, end.distance

    def print_distance_matrix(self, distances: Dict[str, Dict[str, int]]):
        """Вивести матрицю відстаней у зручному форматі"""
        keys = sorted(self._vertices.keys())

        # Заголовок
        header = "     " + "  ".join(f"{k:>4}" for k in keys)
        print(header)
        print("-" * len(header))

        # Рядки
        for from_key in keys:
            row = f"{from_key:>4} |"
            for to_key in keys:
                dist = distances[from_key][to_key]
                if dist == float('inf'):
                    row += f"  {'∞':>3}"
                else:
                    row += f"  {dist:>3}"
            print(row)


# ============== Оптимізована версія з використанням матриці ==============

class AllPairsShortestPath:
    """
    Окремий клас для all-pairs shortest path
    з оптимізованим зберіганням у матриці
    """

    def __init__(self, graph: Graph):
        self.graph = graph
        self.vertices = list(graph.get_vertex_keys())
        self.n = len(self.vertices)
        self.key_to_idx = {key: i for i, key in enumerate(self.vertices)}
        self.distance_matrix = [[float('inf')] * self.n for _ in range(self.n)]
        self.path_matrix = [[None] * self.n for _ in range(self.n)]

    def compute(self):
        """Обчислити всі найкоротші шляхи"""
        for i, vertex_key in enumerate(self.vertices):
            self._bfs_from_vertex(i, vertex_key)

    def _bfs_from_vertex(self, start_idx: int, start_key: str):
        """BFS від однієї вершини"""
        # Ініціалізація
        visited = [False] * self.n
        self.distance_matrix[start_idx][start_idx] = 0
        visited[start_idx] = True

        queue = deque([start_key])

        while queue:
            current_key = queue.popleft()
            current_idx = self.key_to_idx[current_key]
            current_vertex = self.graph.get_vertex(current_key)

            for neighbor in current_vertex.get_neighbors():
                neighbor_idx = self.key_to_idx[neighbor.key]

                if not visited[neighbor_idx]:
                    visited[neighbor_idx] = True
                    self.distance_matrix[start_idx][neighbor_idx] = \
                        self.distance_matrix[start_idx][current_idx] + 1
                    self.path_matrix[start_idx][neighbor_idx] = current_idx
                    queue.append(neighbor.key)

    def get_distance(self, from_key: str, to_key: str) -> int:
        """Отримати відстань між двома вершинами"""
        i = self.key_to_idx.get(from_key)
        j = self.key_to_idx.get(to_key)
        if i is None or j is None:
            return float('inf')
        return self.distance_matrix[i][j]

    def get_path(self, from_key: str, to_key: str) -> List[str]:
        """Отримати найкоротший шлях між двома вершинами"""
        i = self.key_to_idx.get(from_key)
        j = self.key_to_idx.get(to_key)

        if i is None or j is None:
            return []

        if self.distance_matrix[i][j] == float('inf'):
            return []

        # Відновити шлях
        path = [to_key]
        current = j

        while current != i:
            prev = self.path_matrix[i][current]
            if prev is None:
                break
            path.append(self.vertices[prev])
            current = prev

        path.reverse()
        return path

    def print_matrix(self):
        """Вивести матрицю відстаней"""
        header = "     " + "  ".join(f"{k:>4}" for k in self.vertices)
        print(header)
        print("-" * len(header))

        for i, from_key in enumerate(self.vertices):
            row = f"{from_key:>4} |"
            for j in range(self.n):
                dist = self.distance_matrix[i][j]
                if dist == float('inf'):
                    row += f"  {'∞':>3}"
                else:
                    row += f"  {dist:>3}"
            print(row)


# ============== Демонстрація ==============

def demo():
    """Демонстрація роботи All-Pairs Shortest Path"""
    print("=" * 60)
    print("TASK 2: All-Pairs Shortest Path using BFS")
    print("=" * 60)

    # Створюємо тестовий граф (неорієнтований)
    g = Graph()

    # Граф:
    #
    #     A --- B --- C
    #     |     |     |
    #     D --- E --- F
    #           |
    #           G
    #

    edges = [
        ('A', 'B'), ('A', 'D'),
        ('B', 'C'), ('B', 'E'),
        ('C', 'F'),
        ('D', 'E'),
        ('E', 'F'), ('E', 'G'),
    ]

    for v1, v2 in edges:
        g.add_edge(v1, v2, bidirectional=True)

    print("\nГраф (неорієнтований):")
    print("Ребра:", edges)

    # Метод 1: Базова реалізація
    print("\n" + "-" * 40)
    print("Метод 1: Базова реалізація")
    print("-" * 40)

    all_distances = g.all_pairs_shortest_path_bfs()

    print("\nМатриця найкоротших відстаней:")
    g.print_distance_matrix(all_distances)

    # Приклади шляхів
    print("\nПриклади найкоротших шляхів:")
    test_pairs = [('A', 'F'), ('A', 'G'), ('D', 'C'), ('G', 'A')]
    for start, end in test_pairs:
        path, dist = g.get_shortest_path(start, end)
        print(f"  {start} -> {end}: шлях = {' -> '.join(path)}, довжина = {dist}")

    # Метод 2: Оптимізована реалізація з матрицею
    print("\n" + "-" * 40)
    print("Метод 2: Оптимізована реалізація")
    print("-" * 40)

    apsp = AllPairsShortestPath(g)
    apsp.compute()

    print("\nМатриця найкоротших відстаней:")
    apsp.print_matrix()

    print("\nПриклади найкоротших шляхів:")
    for start, end in test_pairs:
        path = apsp.get_path(start, end)
        dist = apsp.get_distance(start, end)
        print(f"  {start} -> {end}: шлях = {' -> '.join(path)}, довжина = {dist}")

    # Приклад з орієнтованим графом
    print("\n" + "=" * 60)
    print("Приклад з орієнтованим графом")
    print("=" * 60)

    g2 = Graph()
    # Орієнтований граф
    directed_edges = [
        (1, 2), (1, 3),
        (2, 4),
        (3, 4), (3, 5),
        (4, 5),
    ]

    for v1, v2 in directed_edges:
        g2.add_edge(v1, v2)  # Тільки в одному напрямку

    print("\nРебра (орієнтовані):", directed_edges)

    all_dist2 = g2.all_pairs_shortest_path_bfs()
    print("\nМатриця найкоротших відстаней:")
    g2.print_distance_matrix(all_dist2)

    print("\nПримітка: ∞ означає, що шлях не існує")


def demo_word_ladder():
    """Демонстрація на прикладі Word Ladder"""
    print("\n" + "=" * 60)
    print("Приклад: Word Ladder з vocabulary.txt")
    print("=" * 60)

    # Завантажити словник і побудувати граф
    try:
        g = build_word_ladder_graph("vocabulary.txt")
        print(f"\nПобудовано граф з {len(g)} вершин")

        # Приклади пошуку шляхів
        test_words = [
            ("FOOL", "SAGE"),
            ("COLD", "WARM"),
            ("LOVE", "HATE"),
        ]

        print("\nПриклади найкоротших шляхів між словами:")
        for start, end in test_words:
            if start in g and end in g:
                path, dist = g.get_shortest_path(start, end)
                if path:
                    print(f"\n  {start} -> {end} (довжина {dist}):")
                    print(f"    {' -> '.join(path)}")
                else:
                    print(f"\n  {start} -> {end}: шлях не знайдено")
            else:
                missing = []
                if start not in g:
                    missing.append(start)
                if end not in g:
                    missing.append(end)
                print(f"\n  Слова {missing} не знайдено в словнику")

    except FileNotFoundError:
        print("\nФайл vocabulary.txt не знайдено")


def build_word_ladder_graph(file_path: str) -> Graph:
    """Побудувати граф Word Ladder зі словника"""
    buckets: Dict[str, List[str]] = {}
    g = Graph()

    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            if not word:
                continue

            # Створити "бакети" для слів, що відрізняються на одну літеру
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in buckets:
                    buckets[bucket].append(word)
                else:
                    buckets[bucket] = [word]

    # Додати ребра для слів у одному бакеті
    for bucket, words in buckets.items():
        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    g.add_edge(word1, word2, bidirectional=True)

    return g


if __name__ == "__main__":
    demo()
    demo_word_ladder()
