import os
from solution import SOLUTION
import constants as c
import copy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm body*.urdf")
        self.nextAvailableID = 0
        self.parents = {}
        # self.parent = SOLUTION()
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
    def Evolve(self):
        self.Evaluate(self.parents, 0)
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
    
    def Evolve_For_One_Generation(self):
        pass
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, 1)
        # self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for k in self.parents:
            self.children[k] = copy.deepcopy(self.parents[k])
            self.children[k].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

        # self.child = copy.deepcopy(self.parent) 
        # self.child.Set_ID(self.nextAvailableID)
        # self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for l in self.children:
            self.children[l].Mutate()
        # self.child.Mutate()

    def Select(self):
         for n in self.parents:
            if(self.parents[n].fitness > self.children[n].fitness):
                self.parents[n] = self.children[n]

    def Print(self):
        for m in self.parents:
            print("Parent's fitness : ", self.parents[m].fitness,"  | Child's fitness : ", self.children[m].fitness)

    def Show_Best(self):
        best = float('inf')
        alpha = None
        for o in self.parents:
            if best > self.parents[o].fitness:
                best = self.parents[o].fitness
                alpha = o
        print("Besttttt:",self.parents[alpha].fitness)
        self.parents[alpha].Start_Simulation("GUI")
        # self.parent.Evaluate("GUI")

    def Evaluate(self, solutions, child_true):
        for i in solutions:
           solutions[i].Start_Simulation("DIRECT", child_true)
        for j in solutions:
            solutions[j].Wait_For_Simulation_To_End()
        pass
        