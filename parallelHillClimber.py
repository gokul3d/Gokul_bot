from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.solutions = {}  # Assuming this is the empty dictionary creation you mentioned
        self.nextAvailableID = 0
        for i in range(c.populationSize):  # Iterating from 0 to c.populationSize-1 inclusive
            self.solutions[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        pass


    def Evolve(self):

        for i in range(len(self.solutions)):
            self.solutions[i].Evaluate("GUI")  # Assuming Evaluate method exists and "DIRECT" is a valid argument

            # Other evolutionary steps would go here, but are commented out for now
        pass

    def Evolve_For_One_Generation(self):
        # self.Spawn()
        # self.Mutate()
        # self.child.Evaluate("DIRECT")
        # self.Print()
        # self.Select()
        pass

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1  # Ensure the next solution gets a new unique ID

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent =  self.child

    def Print(self):
        print('Parent:', self.parent.fitness, '<', 'Child', self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")
