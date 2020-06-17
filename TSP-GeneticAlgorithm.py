import numpy
import random
import math


class City:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

def pathCost (route):
    for i in range(len(route)):
        # Distance between every city
        if i >= len(route)-1:
            break
        else:
            dist = numpy.sqrt(((route[i].x - route[i+1].x) ** 2) + ((route[i].y - route[i+1].y) ** 2))
            distance =+ dist
    
    # Distance between first and last city
    distance =+ numpy.sqrt(((route[0].x - route[-1].x) ** 2) + ((route[0].y - route[-1].y) ** 2))
    return distance

def initialPopulation (n, cities):
    init_pop = list()
    for i in range(n):
        route = random.sample(cities, len(cities))
        init_pop.append(route)

    return init_pop

def evaluatefitness (pop):
    fitness = list()
    for n in range(len(pop)):
        fitness.append(pathCost(pop[n]))

    return fitness

def rankedRoutes (fitnessValues, population):
    zippedList = list(zip(population, fitnessValues))
    pop, fitness = map(list, zip(*sorted(zippedList, key = lambda x: x[1])))

    return pop

def selection (goodSize, fitessValues, population):
    selected = list()
    for i in range(goodSize):
        selected.append(population[i])

    return selected

def offspringCrossover (selection, goodSize):

    offsprings = list()

    for i in range(100 - goodSize):
        P1 = random.choice(selection)
        P2 = random.choice(selection)

        C1 = list(P1[0:math.floor(len(P1)/2)])
        for j in P2:
            if j not in C1:
                C1.append(j)
        offsprings.append(C1)

        C2 = list(P2[0:math.floor(len(P2)/2)])
        for j in P1:
            if j not in C2:
                C2.append(j)
        offsprings.append(C2)

    return offsprings


def mutation (population, goodSize, offsprings):
    offsprings = random.sample(offsprings, len(offsprings))
    nextGeneration = population

    for i in range(goodSize, len(population)):
        nextGeneration[i] = offsprings[i]

    return nextGeneration



# List of cities

cities = list()

Ajmer = City(45, 78, 'Ajmer')
cities.append(Ajmer)

Alwar = City(33, 67, 'Alwar')
cities.append(Alwar)

Bharatpur = City(28, 30, 'Bharatpur')
cities.append(Bharatpur)

Bikaner = City(15, 34, 'Bikaner')
cities.append(Bikaner)

Bundi = City(34, 90, 'Bundi')
cities.append(Bundi)

Chittaurgarh = City(56, 45, 'Chittaurgarh')
cities.append(Chittaurgarh)

Bundi = City(25, 67, 'Bundi')
cities.append(Bundi)

Jaipur = City(68, 55, 'Jaipur')
cities.append(Jaipur)

Jodhpur = City(54, 10, 'Jodhpur')
cities.append(Jodhpur)

Jaisalmer = City(23, 62, 'Jaisalmer')
cities.append(Jaisalmer)

Kota = City(48, 20, 'Kota')
cities.append(Kota)



populationSize = 100
goodSize = 20
generations = 100

population = initialPopulation(populationSize, cities)

print("Initial Route")
initialRoute = population[0]
initialDistance = pathCost(initialRoute)

for i in initialRoute:
    print(str(i.name) + " -> ", end = "")

print()
print("Initial Distance = " + str(initialDistance))
print()


for i in range(generations):
    fitness = evaluatefitness(population)
    rankedPopulation = rankedRoutes(fitness, population)
    selectedParents = selection(goodSize, fitness, rankedPopulation)
    offsprings = offspringCrossover(selectedParents, goodSize)
    nextGeneration = mutation(rankedPopulation, goodSize, offsprings)
    population = nextGeneration

print("Final Route")
finalRoute = nextGeneration[0]
finalDistance = pathCost(finalRoute)

for i in finalRoute:
    print(str(i.name) + " -> ", end = "")

print()
print("Final Distance = " + str(finalDistance))