import os
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import constants as c



class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
        self.myID = nextAvailableID
        # print(self.weights, "weightssss")
        # exit()


    # def Evaluate(self, DIR_GUI):
    #     self.Create_World() 
    #     self.Create_Body()
    #     self.Create_Brain()
    #     os.system("python3 simulate.py " + str(DIR_GUI) + " " + str(self.myID) + " &")
    #     while not os.path.exists("fitness"+str(self.myID)+".txt"):
    #         time.sleep(0.01)
    #     fitnessFile = open("fitness"+str(self.myID)+".txt", "r")
    #     self.fitness = float(fitnessFile.readline())
    #     print( self.fitness, "lollllol")
    #     fitnessFile.close()

    def Start_Simulation(self, DIR_GUI):
        self.Create_World() 
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + str(DIR_GUI) + " " + str(self.myID) + " &")
        

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        fitnessFile = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(fitnessFile.readline())
        fitnessFile.close()
        # print( self.myID, self.fitness)
        os.system("rm fitness"+str(self.myID)+".txt")
        
       
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x = -3
        y = 3
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.End()


    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )

        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -1.0 )

        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                    pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        # randomRow - three sensor neurons
        randomRow =  random.randint(0,c.numSensorNeurons - 1)
        # randomColumn - two motor neurons
        randomColumn = random.randint(0,c.numMotorNeurons - 1)
        self.weights[randomRow,randomColumn] =  random.random() * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        pass


            