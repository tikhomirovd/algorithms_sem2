import numpy as np


def fitness(x):
    return x ** 2


def crossover(parent1, parent2):
    return (parent1 + parent2) / 2


def mutate(child, mutation_rate):
    if np.random.random() < mutation_rate:
        child += np.random.normal()
    return child


def genetic_algorithm(population_size, mutation_rate, n_generations):
    population = np.random.uniform(-10, 10, population_size)
    fitness_scores = []
    for generation in range(n_generations):
        fitness_scores = [fitness(individual) for individual in population]

        # Выбираем двух родителей с вероятностью, пропорциональной их приспособленности
        parents = population[
            np.random.choice(range(population_size), size=2, p=fitness_scores / np.sum(fitness_scores))]

        child = mutate(crossover(parents[0], parents[1]), mutation_rate)

        min_fitness_idx = np.argmin(fitness_scores)
        population[min_fitness_idx] = child

        max_fitness_idx = np.argmax(fitness_scores)
        print(
            f"Generation {generation + 1} - x: {population[max_fitness_idx]}, fitness: {fitness_scores[max_fitness_idx]}")

    return population[np.argmax(fitness_scores)]


population_size = 10
mutation_rate = 0.1
n_generations = 100

best_individual = genetic_algorithm(population_size, mutation_rate, n_generations)
print(best_individual)