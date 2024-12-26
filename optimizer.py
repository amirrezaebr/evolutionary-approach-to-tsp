from individual import Individual
from evaluation import evaluate, evaluate_all
from selection import tournament_selection
from crossover import cross_over
from mutation import mutation
from termination_condition import terminate
import random


def run_algorithm(
        distance_matrix,
        population_size=20,
        generation_size=30,
):
    MUTATION_RATE = 0.3
    best_fitness_list = []
    avg_fitness_list = []
    best_individual = None
    genome_size = len(distance_matrix)

    # create primary population
    population = primary_population_creator(population_size, genome_size)
    evaluate_all(population)
    while True:
        # cross over
        generated_individuals = []
        for _ in range(int(generation_size / 2)):
            parent1 = tournament_selection(population, 4)
            parent2 = tournament_selection(population, 4)
            child1, child2 = cross_over(parent1, parent2)
            child1.fitness = evaluate(child1)
            child2.fitness = evaluate(child2)
            generated_individuals.append(child1)
            generated_individuals.append(child2)

        # mutation
        for individual in generated_individuals:
            if random.random() <= MUTATION_RATE:
                individual.genome = mutation(individual)

        evaluate_all(generated_individuals)
        population = next_generation_selection(generated_individuals, population)

        if type(terminate(population)) == float:
            break

        # don't change following codes
        best_fitness_list.append(best_fitness(population))
        avg_fitness_list.append(avg_fitness(population))
        random.shuffle(population)

    return best_individual, best_fitness_list, avg_fitness_list


def primary_population_creator(
        population_size: int, genome_size: int
) -> list[Individual]:
    population = []
    for _ in range(population_size):
        population.append(Individual(genome_size, True))
    return population


def avg_fitness(
        population: list[Individual]
) -> float:
    total_fitness = 0

    for individual in population:
        total_fitness += individual.fitness
    return total_fitness / len(population)


def best_fitness(
        population: list[Individual]
) -> float:
    max_fitness = 0.0

    for individual in population:
        if individual.fitness > max_fitness:
            max_fitness = individual.fitness
    return max_fitness


def next_generation_selection(generated_individuals: list[Individual], population: list[Individual]) -> list[
    Individual]:
    combined_individuals = generated_individuals + population

    valid_individuals = [ind for ind in combined_individuals if ind.fitness is not None]

    sorted_individuals = sorted(valid_individuals, key=lambda ind: ind.fitness, reverse=True)

    next_generation = sorted_individuals[:len(population)]
    return next_generation
