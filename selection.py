import random
from individual import Individual


def tournament_selection(individual_list: list[Individual], tournament_size: int) -> Individual:
    tournament_individuals = random.sample(individual_list, tournament_size)
    best_individual = max(tournament_individuals, key=lambda ind: ind.fitness)

    return best_individual

