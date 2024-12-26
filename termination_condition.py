def terminate(individual_list):
    BEST_FITNESS = 0.002  # length of the shortest path

    for individual in individual_list:
        if individual.fitness >= BEST_FITNESS:
            return individual.fitness
    return None
