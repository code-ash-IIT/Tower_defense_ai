# general constants
X   = 0
Y   = 1
ON  = True
OFF = False


# AI general constants
NUMBER_OF_STARTING_TOWERS = 15


# GA constants
FITTEST_POPULATION_FRACTION = 3                             # Take 1/5th of the population size for survival of the fittest
POPULATION_SIZE = (FITTEST_POPULATION_FRACTION * 16) * 2   # Must be a multiple of FITTEST_POPULATION_FRACTION, and divisible by 2
MAX_GENERATIONS = 100
MUTATION_PCT = 0.15
SURVIVAL_OF_THE_FITTEST = True
NUMBER_OF_CHILDREN = 2
