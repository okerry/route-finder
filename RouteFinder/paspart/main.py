from password import get_password
from fitness import distance_function, get_normalised_fitness, MAX_VALUE
from population import generate_population
from selection import tournament_selection
from crossover import single_point_crossover
from mutation import mutate

def genetic_algorithm(population_size, password_length, tournament_size, mutation_rate, generations):
    # ... (rest of the function as before)
