from individual import Individual
from dataset_preparation import create_distance_matrix


def evaluate_all(individual_list: list[Individual]):
    for individual in individual_list:
        evaluate(individual)


def evaluate(individual: Individual):
    distance_matrix = create_distance_matrix("tsp")

    # Calculate the total distance for the route described by the individual's genome
    total_distance = 0
    for i in range(len(individual) - 1):
        city_a = individual.genome[i]
        city_b = individual.genome[i + 1]
        total_distance += distance_matrix[city_a][city_b]

    total_distance += distance_matrix[individual.genome[-1]][individual.genome[0]]

    individual.fitness = 1 / total_distance if total_distance > 0 else float('inf')  # Avoid division by zero

    return individual.fitness
