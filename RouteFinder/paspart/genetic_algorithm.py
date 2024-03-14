def genetic_algorithm(mutation_rate=0.01, crossover_rate=0.5, population_size=100):
  student_username = '***'  # replace with your username
  student_password = get_password(student_username)[^2^][2]
  print('Password:', student_password)[^3^][3]

  population = generate_population(population_size, len(student_password))
  for generation in range(1000):
      fitness_scores = get_normalised_fitness(population, student_password)[^4^][4][^5^][5]
      population_sorted = sorted(population, key=lambda x: -fitness_scores[x])
      if population_sorted[0] == student_password:
          print('Found password:', population_sorted[0])
          return generation
      new_population = population_sorted[:population_size//2]
      for _ in range(population_size//4):
          if random.random() < crossover_rate:
              parent1, parent2 = random.sample(new_population, 2)
              child1, child2 = crossover(parent1, parent2)
              new_population += [child1, child2]
      for i in range(len(new_population)):
          if random.random() < mutation_rate:
              new_population[i] = mutate(new_population[i])
      population = new_population
  else:
      print('Did not find password. Best attempt:', population_sorted[0])
      return 1000

# Run the genetic algorithm with different hyperparameters
results = []
for mutation_rate in [0.01, 0.05]:
  for crossover_rate in [0.5, 0.7]:
      for population_size in [100, 200]:
          generations = [genetic_algorithm(mutation_rate, crossover_rate, population_size) for _ in range(10)]
          avg_generations = sum(generations) / len(generations)
          std_generations = math.sqrt(sum((x - avg_generations) ** 2 for x in generations) / len(generations))
          results.append((mutation_rate, crossover_rate, population_size, avg_generations, std_generations))

# Print the results
for mutation_rate, crossover_rate, population_size, avg_generations, std_generations in results:
  print(f'Mutation rate: {mutation_rate}, Crossover rate: {crossover_rate}, Population size: {population_size}, Average generations: {avg_generations}, Standard deviation: {std_generations}')
