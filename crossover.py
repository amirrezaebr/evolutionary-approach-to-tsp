from individual import Individual
import random


def cross_over(parent1: Individual, parent2: Individual):
    child1 = order_crossover(parent1, parent2)
    child2 = order_crossover(parent2, parent1)
    return child1, child2


def order_crossover(parent1: Individual, parent2: Individual):
    size = len(parent1)
    point1, point2 = sorted(random.sample(range(size), 2))
    offspring_genome = [None] * size
    offspring_genome[point1:point2] = parent1.genome[point1:point2]
    current_position = point2

    for gene in parent2.genome:
        if gene not in offspring_genome:
            if current_position == size:
                current_position = 0
            offspring_genome[current_position] = gene
            current_position += 1

    offspring = Individual(generate_random_genome=False)
    offspring.genome = offspring_genome
    return offspring
