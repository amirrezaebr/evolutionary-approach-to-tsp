from individual import Individual
import random


def mutation(individual: Individual):
    index1 = random.randint(0, len(individual.genome) - 1)
    index2 = random.randint(0, len(individual.genome) - 1)
    individual.genome[index1], individual.genome[index2] = individual.genome[index2], individual.genome[index1]
    return individual.genome
