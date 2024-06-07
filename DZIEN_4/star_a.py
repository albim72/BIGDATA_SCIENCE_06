import heapq


def greedy_best_first_search(graph, start, goal, h):
    # Inicjalizacja frontier jako kopca (priority queue)
    frontier = []
    heapq.heappush(frontier, (h(start, goal), start))

    # Słownik przechowujący, skąd przyszliśmy do danego węzła
    came_from = {}
    came_from[start] = None

    while frontier:
        # Pobranie węzła o najmniejszej wartości heurystyki h
        _, current = heapq.heappop(frontier)

        # Jeśli osiągnięto cel, rekonstrukcja ścieżki
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        # Przeglądanie sąsiadów bieżącego węzła
        for neighbor in graph[current]:
            if neighbor not in came_from:
                priority = h(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    return None


def heuristic(a, b):
    # Funkcja heurystyczna - odległość Manhattan
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(1, 0): 1, (0, 1): 1, (2, 2): 1},
    (2, 2): {}
}

start = (0, 0)
goal = (2, 2)
path = greedy_best_first_search(graph, start, goal, heuristic)
print("Path:", path)
