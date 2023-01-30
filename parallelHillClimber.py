import os
from solution import SOLUTION
import constants as c
import copy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        # self.parent = SOLUTION()
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
    def Evolve(self):
        for i in self.parents:
            self.parents[i].Start_Simulation("DIRECT")
        for j in self.parents:
            self.parents[j].Wait_For_Simulation_To_End()
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
            
    
    def Evolve_For_One_Generation(self):
        pass
        self.Spawn()
        # self.Mutate()
        # self.child.Evaluate("DIRECT")
        # self.Print()
        # self.Select()

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
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Print(self):
        print("Parent's fitness : ", self.parent.fitness,"  | Child's fitness : ", self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")
        