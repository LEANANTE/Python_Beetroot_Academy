"""
Task 1: Modify the 'depth-first search' to produce Strongly Connected Components (SCC)

Strongly Connected Component (SCC) - це максимальна підмножина вершин графа,
в якій існує шлях від кожної вершини до кожної іншої.

Використовуємо алгоритм Косарайю (Kosaraju's Algorithm):
1. Виконати DFS на оригінальному графі і записати порядок завершення вершин
2. Транспонувати граф (перевернути всі ребра)
3. Виконати DFS на транспонованому графі в порядку спадання часу завершення
4. Кожне дерево DFS у другому проході - це SCC
"""

import sys
from typing import Dict, List, Optional, Set


class Vertex:
    """Клас вершини графа"""

    def __init__(self, key):
        self._key = key
        self._neighbors: Dict["Vertex", int] = {}
        self._color = "white"
        self._discovery_time = 0
        self._closing_time = 0
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
    def discovery_time(self):
        return self._discovery_time

    @discovery_time.setter
    def discovery_time(self, value):
        self._discovery_time = value

    @property
    def closing_time(self):
        return self._closing_time

    @closing_time.setter
    def closing_time(self, value):
        self._closing_time = value

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
    """Клас графа з підтримкою SCC"""

    def __init__(self):
        self._vertices: Dict[str, Vertex] = {}
        self._time = 0

    def add_vertex(self, key) -> Vertex:
        """Додати вершину до графа"""
        if key not in self._vertices:
            self._vertices[key] = Vertex(key)
        return self._vertices[key]

    def get_vertex(self, key) -> Optional[Vertex]:
        """Отримати вершину за ключем"""
        return self._vertices.get(key, None)

    def add_edge(self, from_key, to_key, weight: int = 0):
        """Додати направлене ребро"""
        if from_key not in self._vertices:
            self.add_vertex(from_key)
        if to_key not in self._vertices:
            self.add_vertex(to_key)
        self._vertices[from_key].add_neighbor(self._vertices[to_key], weight)

    def get_vertices(self):
        """Отримати всі вершини"""
        return self._vertices.values()

    def __iter__(self):
        return iter(self._vertices.values())

    def __contains__(self, key):
        return key in self._vertices

    def reset(self):
        """Скинути стан всіх вершин"""
        self._time = 0
        for vertex in self._vertices.values():
            vertex.color = "white"
            vertex.discovery_time = 0
            vertex.closing_time = 0
            vertex.previous = None

    def dfs(self) -> List[Vertex]:
        """
        Стандартний DFS, що повертає список вершин у порядку завершення
        (потрібно для алгоритму Косарайю)
        """
        self.reset()
        finish_order = []

        for vertex in self._vertices.values():
            if vertex.color == "white":
                self._dfs_visit(vertex, finish_order)

        return finish_order

    def _dfs_visit(self, vertex: Vertex, finish_order: List[Vertex]):
        """Допоміжна функція для DFS"""
        vertex.color = "gray"
        self._time += 1
        vertex.discovery_time = self._time

        for neighbor in vertex.get_neighbors():
            if neighbor.color == "white":
                neighbor.previous = vertex
                self._dfs_visit(neighbor, finish_order)

        vertex.color = "black"
        self._time += 1
        vertex.closing_time = self._time
        finish_order.append(vertex)

    def transpose(self) -> "Graph":
        """
        Створити транспонований граф (всі ребра перевернуті)
        """
        transposed = Graph()

        # Додати всі вершини
        for vertex in self._vertices.values():
            transposed.add_vertex(vertex.key)

        # Додати перевернуті ребра
        for vertex in self._vertices.values():
            for neighbor in vertex.get_neighbors():
                # Було: vertex -> neighbor
                # Стало: neighbor -> vertex
                transposed.add_edge(neighbor.key, vertex.key)

        return transposed

    def find_scc(self) -> List[List[str]]:
        """
        Знайти всі Strongly Connected Components (SCC)
        використовуючи алгоритм Косарайю

        Повертає список SCC, де кожна SCC - це список ключів вершин
        """
        # Крок 1: Виконати DFS і отримати порядок завершення
        finish_order = self.dfs()

        # Крок 2: Створити транспонований граф
        transposed = self.transpose()

        # Крок 3: Виконати DFS на транспонованому графі
        # у зворотньому порядку завершення
        transposed.reset()
        scc_list = []

        # Обробляємо вершини в зворотньому порядку завершення
        for vertex in reversed(finish_order):
            trans_vertex = transposed.get_vertex(vertex.key)
            if trans_vertex.color == "white":
                # Нова SCC
                current_scc = []
                self._dfs_collect_scc(trans_vertex, current_scc)
                scc_list.append(current_scc)

        return scc_list

    def _dfs_collect_scc(self, vertex: Vertex, scc: List[str]):
        """Збирає всі вершини однієї SCC"""
        vertex.color = "gray"
        scc.append(vertex.key)

        for neighbor in vertex.get_neighbors():
            if neighbor.color == "white":
                self._dfs_collect_scc(neighbor, scc)

        vertex.color = "black"


# ============== Альтернативна реалізація: Алгоритм Тар'яна ==============

class TarjanSCC:
    """
    Алгоритм Тар'яна для знаходження SCC
    Використовує один прохід DFS з low-link values
    """

    def __init__(self, graph: Graph):
        self.graph = graph
        self.index_counter = 0
        self.stack = []
        self.lowlinks = {}
        self.index = {}
        self.on_stack = {}
        self.sccs = []

    def find_scc(self) -> List[List[str]]:
        """Знайти всі SCC"""
        # Ініціалізація
        for vertex in self.graph.get_vertices():
            self.lowlinks[vertex.key] = -1
            self.index[vertex.key] = -1
            self.on_stack[vertex.key] = False

        # Запустити DFS для кожної непройденої вершини
        for vertex in self.graph.get_vertices():
            if self.index[vertex.key] == -1:
                self._strongconnect(vertex)

        return self.sccs

    def _strongconnect(self, vertex: Vertex):
        """Допоміжна функція Тар'яна"""
        # Присвоїти найменший невикористаний індекс
        self.index[vertex.key] = self.index_counter
        self.lowlinks[vertex.key] = self.index_counter
        self.index_counter += 1
        self.stack.append(vertex)
        self.on_stack[vertex.key] = True

        # Розглянути всіх сусідів
        for neighbor in vertex.get_neighbors():
            if self.index[neighbor.key] == -1:
                # Сусід ще не відвіданий - рекурсія
                self._strongconnect(neighbor)
                self.lowlinks[vertex.key] = min(
                    self.lowlinks[vertex.key],
                    self.lowlinks[neighbor.key]
                )
            elif self.on_stack[neighbor.key]:
                # Сусід на стеку - це зворотнє ребро
                self.lowlinks[vertex.key] = min(
                    self.lowlinks[vertex.key],
                    self.index[neighbor.key]
                )

        # Якщо vertex - корінь SCC, вивантажити стек
        if self.lowlinks[vertex.key] == self.index[vertex.key]:
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack[w.key] = False
                scc.append(w.key)
                if w.key == vertex.key:
                    break
            self.sccs.append(scc)


# ============== Демонстрація ==============

def demo():
    """Демонстрація роботи алгоритмів SCC"""
    print("=" * 60)
    print("TASK 1: Strongly Connected Components (SCC)")
    print("=" * 60)

    # Створюємо тестовий граф
    g = Graph()

    # Приклад графа з кількома SCC:
    #
    #     ┌──────────┐
    #     ↓          │
    #     A ──→ B ──→ C
    #     ↑     │
    #     │     ↓
    #     E ←── D ──→ F ──→ G
    #                 ↑     │
    #                 └─────┘
    #
    # SCC: {A, B, D, E}, {C}, {F, G}

    edges = [
        ('A', 'B'),
        ('B', 'C'),
        ('B', 'D'),
        ('C', 'A'),
        ('D', 'E'),
        ('D', 'F'),
        ('E', 'A'),
        ('F', 'G'),
        ('G', 'F'),
    ]

    for from_v, to_v in edges:
        g.add_edge(from_v, to_v)

    print("\nГраф:")
    print("Ребра:", edges)

    # Метод 1: Алгоритм Косарайю
    print("\n" + "-" * 40)
    print("Метод 1: Алгоритм Косарайю")
    print("-" * 40)

    scc_kosaraju = g.find_scc()
    print(f"\nЗнайдено {len(scc_kosaraju)} SCC:")
    for i, scc in enumerate(scc_kosaraju, 1):
        print(f"  SCC {i}: {scc}")

    # Метод 2: Алгоритм Тар'яна
    print("\n" + "-" * 40)
    print("Метод 2: Алгоритм Тар'яна")
    print("-" * 40)

    tarjan = TarjanSCC(g)
    scc_tarjan = tarjan.find_scc()
    print(f"\nЗнайдено {len(scc_tarjan)} SCC:")
    for i, scc in enumerate(scc_tarjan, 1):
        print(f"  SCC {i}: {scc}")

    # Додатковий приклад
    print("\n" + "=" * 60)
    print("Додатковий приклад: Простий цикл")
    print("=" * 60)

    g2 = Graph()
    # Простий цикл: 1 -> 2 -> 3 -> 1
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 1)
    # Окрема вершина: 4 -> 5
    g2.add_edge(4, 5)

    print("\nРебра: 1->2, 2->3, 3->1, 4->5")
    scc2 = g2.find_scc()
    print(f"\nЗнайдено {len(scc2)} SCC:")
    for i, scc in enumerate(scc2, 1):
        print(f"  SCC {i}: {scc}")


if __name__ == "__main__":
    demo()
