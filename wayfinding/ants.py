import numpy as np
import random

n_ants = 100
n_cities = 20
n_iterations = 200
decay = 0.6  # коэффициент испарения
alpha = 1  # вес феромона
beta = 1  # вес длины пути
distances = np.random.randint(1, 100, (n_cities, n_cities))
pheromones = np.ones((n_cities, n_cities))


# Главная функция
def ant_colony_optimization():
    shortest_path = None
    min_path_len = float('inf')

    for i in range(n_iterations):
        all_paths = construct_solutions()
        shortest_path_iter, min_path_len_iter = find_shortest_path(all_paths)
        if min_path_len_iter < min_path_len:
            shortest_path = shortest_path_iter
            min_path_len = min_path_len_iter
        update_pheromones(all_paths)

    return shortest_path, min_path_len


def construct_solutions():
    all_paths = []
    for i in range(n_ants):
        path = [random.randint(0, n_cities - 1)]
        while len(path) < n_cities:
            current_city = path[-1]
            next_city = choose_next_city(current_city, path)
            path.append(next_city)
        all_paths.append((path, compute_path_len(path)))
    return all_paths


def choose_next_city(current_city, path):
    probabilities = []
    for city in range(n_cities):
        if city not in path:
            tau = pheromones[current_city][city] ** alpha
            eta = (1.0 / distances[current_city][city]) ** beta
            probabilities.append(tau * eta)
        else:
            probabilities.append(0)
    probabilities = [p / sum(probabilities) for p in probabilities]
    return np.random.choice(range(n_cities), 1, p=probabilities)[0]


def compute_path_len(path):
    return sum([distances[path[i]][path[i + 1]] for i in range(len(path) - 1)]) + distances[path[-1]][path[0]]


def find_shortest_path(paths):
    min_len = float('inf')
    shortest_path = None
    for path, length in paths:
        if length < min_len:
            min_len = length
            shortest_path = path
    return shortest_path, min_len


def update_pheromones(paths):
    for i in range(n_cities):
        for j in range(n_cities):
            pheromones[i][j] *= decay
            for path, length in paths:
                if i in path and j in path:
                    pheromones[i][j] += 1.0 / length


# Запуск алгоритма
shortest_path, min_path_len = ant_colony_optimization()
print(f"Shortest path: {shortest_path}, length: {min_path_len}")
