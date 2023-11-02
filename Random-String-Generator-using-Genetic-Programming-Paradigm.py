import random

def generate_string(length):
  """Generates a random string of the given length."""
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  string = ""
  for i in range(length):
    string += random.choice(chars)
  return string

def fitness_function(string, target_string):
  """Calculates the fitness of the given string, where the fitness is the number of characters that match the target string."""
  fitness = 0
  for i in range(len(string)):
    if string[i] == target_string[i]:
      fitness += 1
  return fitness

def genetic_algorithm(target_string, population_size, crossover_rate, mutation_rate, max_generations):
  """Evolves a population of strings to match the target string using a genetic algorithm."""
  population = []
  for i in range(population_size):
    population.append(generate_string(len(target_string)))

  generation = 0
  while generation < max_generations:
    # Select parents
    parents = []
    for i in range(population_size):
      parent1 = random.choice(population)
      parent2 = random.choice(population)
      parents.append((parent1, parent2))

    # Crossover
    children = []
    for parent1, parent2 in parents:
      child = ""
      for i in range(len(target_string)):
        if random.random() < crossover_rate:
          child += parent1[i]
        else:
          child += parent2[i]
      children.append(child)

    # Mutation
    for child in children:
      for i in range(len(target_string)):
        if random.random() < mutation_rate:
          child = child[:i] + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") + child[i + 1:]

    # Evaluate fitness
    fitness_scores = []
    for child in children:
      fitness_scores.append(fitness_function(child, target_string))

    # Select the best individuals for the next generation
    new_population = []
    for i in range(population_size):
      best_individual = children[fitness_scores.index(max(fitness_scores))]
      new_population.append(best_individual)

    # Replace the old population with the new population
    population = new_population

    # Increment the generation counter
    generation += 1

  # Return the best individual in the population
  best_individual = population[fitness_scores.index(max(fitness_scores))]
  return best_individual

# Set the target string
target_string = "Hello, world!"

# Set the genetic algorithm parameters
population_size = 100
crossover_rate = 0.7
mutation_rate = 0.01
max_generations = 100

# Run the genetic algorithm 10 times
for _ in range(10):
    best_string = genetic_algorithm(target_string, population_size, crossover_rate, mutation_rate, max_generations)
    print(best_string)
