import numpy as np

# Параметры задачи
weights = np.array([2, 3, 4, 5, 6, 7, 1, 2])
values = np.array([3, 4, 5, 6, 1, 10, 3, 2])
max_weight = 7


def fitness(individual, weights, values, max_weight):
    total_weight = np.sum(individual * weights)
    total_value = np.sum(individual * values)

    if total_weight > max_weight:
        return 0
    return total_value


def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2


def mutate(child):
    mutation_point = np.random.randint(len(child))
    child[mutation_point] = 1 - child[mutation_point]
    return child


def genetic_algorithm(weights, values, max_weight, pop_size, n_generations, mutation_rate):
    n_items = len(weights)

    population = np.random.randint(2, size=(pop_size, n_items))

    for generation in range(n_generations):
        # Оцениваем приспособленность каждой хромосомы
        fitness_scores = [fitness(ind, weights, values, max_weight) for ind in population]

        new_population = []
        for i in range(pop_size // 2):
            # Селекция
            selected_indices = np.random.choice(range(pop_size), size=2, p=fitness_scores / np.sum(fitness_scores))
            parent1, parent2 = population[selected_indices]

            # Скрещивание
            child1, child2 = crossover(parent1, parent2)

            # Мутация
            if np.random.random() < mutation_rate:
                child1 = mutate(child1)
                child2 = mutate(child2)

            new_population.extend([child1, child2])

        population = np.array(new_population)

    best_idx = np.argmax([fitness(ind, weights, values, max_weight) for ind in population])
    return population[best_idx]


pop_size = 50
n_generations = 100
mutation_rate = 0.2

best_solution = genetic_algorithm(weights, values, max_weight, pop_size, n_generations, mutation_rate)
print(f"Best solution: {best_solution}")
print(f"Total value: {np.sum(best_solution * values)}")
