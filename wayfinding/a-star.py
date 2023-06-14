import heapq
import matplotlib.pyplot as plt
import numpy as np


def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def a_star_search(graph, start, goal):
    pq = [(0, start)]
    came_from = {start: None}
    g_score = {start: 0}
    visited = set()

    while pq:
        current_f, current = heapq.heappop(pq)

        if current == goal:
            return reconstruct_path(came_from, start, goal), visited

        for neighbor in graph.get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                visited.add(neighbor)
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_score, neighbor))
                came_from[neighbor] = current

    return None, visited


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, pos):
        return pos not in self.walls

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [n for n in neighbors if self.in_bounds(n) and self.passable(n)]


grid = Grid(10, 10)
grid.walls = [(3, 3), (3, 4), (4, 3), (4, 4), (2, 2), (1, 2), (2, 1), (7, 1), (1, 7)]
start, goal = (1, 1), (7, 7)
path, visited = a_star_search(grid, start, goal)

# Visualizing
grid_map = np.zeros((grid.height, grid.width, 3))
for x, y in visited:
    grid_map[y, x] = [0.5, 0.5, 0.5]  # Gray for visited
for x, y in path:
    grid_map[y, x] = [0, 1, 0]  # Green for path
for x, y in grid.walls:
    grid_map[y, x] = [1, 0, 0]  # Red for walls
grid_map[start[1], start[0]] = [0, 0, 1]  # Blue for start
grid_map[goal[1], goal[0]] = [1, 1, 0]  # Yellow for goal

plt.imshow(grid_map)
plt.axis('off')
plt.show()
