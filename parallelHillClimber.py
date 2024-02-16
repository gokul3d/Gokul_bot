from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system('del brain*.nndf')
        os.system('del fitness*.txt')
        self.parents = {}
        #self.children = {}
        self.solutions = {}  # Assuming this is the empty dictionary creation you mentioned
        self.nextAvailableID = 0
        for i in range(c.populationSize):  # Iterating from 0 to c.populationSize-1 inclusive
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1




    def Evolve(self):

        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()




    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()


    def Spawn(self):
        # Check if self.parents is empty
        if not self.parents:
            print("No parents available to spawn children.")
            return  # Exit the method early if there are no parents

        self.children = {}
        for i in range(len(self.parents)):
            # Copy the parent first before setting the ID on the copy (child)
            self.children[i] = copy.deepcopy(self.parents[i])
            # Now set the unique ID on the child, not the original parent
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            # Print the child's ID for verification
        #     print(f"Child {i}: ID {self.children[i].myID}")
        # exit()

    def Mutate(self):

        for child in range(len(self.children)):
            self.children[child].Mutate()

    def Select(self):
        for key in range(len(self.parents)):
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] =  self.children[key]

    def Print(self):
        print('\n')
        for key in range(len(self.parents)):
            print('Parent:', self.parents[key].fitness, '<', 'Child:', self.children[key].fitness)
        print('\n')

    def Show_Best(self):
        if not self.parents:  # Check if the parents list is empty
            print("No parents to show.")
            return

        bestKey = 0
        bestFit = self.parents[0].fitness
        for key in range(1, len(self.parents)):  # Start from 1 since 0 is the initial assumption
            if self.parents[key].fitness < bestFit:
                bestFit = self.parents[key].fitness
                bestKey = key
        print(f"Best Fitness: {bestFit}")
        print(f"Best Key: {bestKey}")
        # Assuming Start_Simulation method of the SOLUTION class is correctly implemented
        # to visualize the solution.
        self.parents[bestKey].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT")
            # Assuming Evaluate method exists and "DIRECT" is a valid argument

            # Other evolutionary steps wouldhere, but are commented out for now
            # "comment this to turn off parallelism off"
        for i in range(len(solutions)):
            solutions[i].Wait_For_Simulation_To_End()


