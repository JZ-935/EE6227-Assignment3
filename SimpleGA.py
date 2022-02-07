# Python3 program to solve 8 queens problem, starting from
# random string using Genetic Algorithm

import random
import numpy
import os

# Number of individuals in each generation
POPULATION_SIZE = int(input("Choose your population size: "))

N_raw = input('Decide your chessboard size(an integer greater than 3): ')
if N_raw.isdigit():
 	N = int(N_raw)
else:
 	raise Exception("Input Wrong")

GENES = list(range(1, N+1))


class Individual(object):
	'''
	Class representing individual in population
	'''
	def __init__(self, chromosome):
		self.chromosome = chromosome
		self.fitness = self.FitnessClaculation()

	@classmethod
	def CreateChromosome(self):
		'''
		create chromosome
		'''
		global GENES
		Chromosome = GENES
		random.shuffle(Chromosome)
		return Chromosome

	def Crossover(self, Parent2):
		'''
		Crossover operation 
		'''
		global GENES
		CrossoverPoint = random.randint(1,len(GENES)-1) 
		
		ChildrenChromosome1 = self.chromosome[0 : CrossoverPoint]
		ChildrenChromosome2 = Parent2.chromosome[0 : CrossoverPoint]
		
		ChildrenChromosome1 += [x for x in self.chromosome if x not in ChildrenChromosome1]
		ChildrenChromosome2 += [x for x in Parent2.chromosome if x not in ChildrenChromosome2]
		
		
		return Individual(ChildrenChromosome1), Individual(ChildrenChromosome2)


	def Mutation(self):
		'''
		Mutation operation 
		'''
		global GENES
		position = GENES
		random.shuffle(position)
		position1 = position[0]
		position2 = position[1]
		
		self.chromosome[position1-1], self.chromosome[position2-1] =\
			self.chromosome[position2-1], self.chromosome[position1-1]
		self.fitness = self.FitnessClaculation()

	
	
	def FitnessClaculation(self):
		'''
		Calculate fittness score, it is the number of
		queens in attack positions.
		'''
		global GENES
		fitness = 0
		UpperLeftDiagonal = numpy.zeros((len(GENES),), dtype = int)
		UpperRightDiagonal = numpy.zeros((len(GENES),), dtype = int)
		RepetitionCount = []
		
		for index in range(len(UpperLeftDiagonal)):
			UpperLeftDiagonal[index] = self.chromosome[index] - index - 1
			UpperRightDiagonal[index] = self.chromosome[index] - len(GENES) + index
		#print("UpperLeftDiagonal: %s"%UpperLeftDiagonal)
		#print("UpperRightDiagonal: %s"%UpperRightDiagonal)
		
		# calculate attacking queens 
		# temp = 0
		for index in range(len(UpperLeftDiagonal)):
			for i in range(len(UpperLeftDiagonal)):
				if i != index and \
					(UpperLeftDiagonal[index] == UpperLeftDiagonal[i] \
					  or UpperRightDiagonal[index] == UpperRightDiagonal[i]):
						if (i+1) not in RepetitionCount:
							RepetitionCount.append(i + 1)
							#print(RepetitionCount)
							#temp += 1
		fitness = len(RepetitionCount)
		
		return fitness

# Driver code
def main():
	global POPULATION_SIZE

	#current generation
	generation = 1

	population = []
	Newpopulation = []

	# create initial population
	for _ in range(POPULATION_SIZE):
		Chromosome = Individual.CreateChromosome()
		population.append(Individual(Chromosome))

	# sort the population in increasing order of fitness score
	population = sorted(population, key = lambda x:x.fitness)
	
	while population[0].fitness:
		probability = random.random()
		index = 0
		while index < POPULATION_SIZE - 1:
			children1, children2 = population[index].Crossover(population[index+1])
			Newpopulation.append(children1)
			Newpopulation.append(children2)
			index += 2
		if probability < 0.8:
			index = 0
			while index < 0.2 * POPULATION_SIZE:
				Choice = random.randint(0,POPULATION_SIZE-1)
				Newpopulation[Choice].Mutation()
				index += 1
		population = sorted(Newpopulation, key = lambda x:x.fitness)
		generation += 1
		print("Generations:%d Configuration:%s Attacking queens number:%d"\
		%(generation, population[0].chromosome, population[0].fitness))
	if generation == 1:
		print("Generations: %d\tConfiguration: %s\tAttacking queens number: %d"\
		   %(generation, population[0].chromosome, population[0].fitness))
	os.system("pause")

if __name__ == '__main__':
	main()