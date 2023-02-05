from simulation import SIMULATION
import sys

directOrGUI =  sys.argv[1]
solutionID = sys.argv[2]
x = sys.argv[3]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run(int(x))
simulation.Get_Fitness(solutionID)