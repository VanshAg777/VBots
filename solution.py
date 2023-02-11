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
        y = 10
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        height = random.randint(1,3) * numpy.random.rand()
        color = 0
        r = 0
        g = 1
        b = 1

        linkLenInfo = {}

        for i in range(0,c.numLinks):
            length = random.randint(1,3) * numpy.random.rand()
            width = random.randint(1,3) * numpy.random.rand()
            if (c.randSensorsList[i] == 1):
                b = 0

            if (i == 0):
                pyrosim.Send_Cube(name = "Link" + str(i), pos=[0,0,0] , size=[length,width,height], mass = 1)
            else:
                pyrosim.Send_Cube(name = "Link" +str(i), pos=[length/2,0,0] , size=[length,width,height], mass = 1)

            linkLenInfo["Link" + str(i)] = length
            
        for j in range(1,c.numLinks):
            if (j == 1):
                pyrosim.Send_Joint(name = "Link" + str(j-1) + "_" + "Link" + str(j) , parent = "Link" + str(j-1) , child = "Link" + str(j) , type = "revolute", position = [linkLenInfo["Link" + str(j-1)]/2,0,0], jointAxis = "0 0 1")
            else:
                pyrosim.Send_Joint(name = "Link" + str(j-1) + "_" + "Link" + str(j) , parent = "Link" + str(j-1) , child = "Link" + str(j) , type = "revolute", position = [linkLenInfo["Link" + str(j-1)],0,0], jointAxis = "0 0 1")



        pyrosim.End()


    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        
        counter = 0
        for i in range(0,c.numLinks):
            if (c.randSensorsList[i] == 1):
                pyrosim.Send_Sensor_Neuron(name = counter , linkName = "Link" + str(i))
                counter += 1

        for j in range(1,c.numLinks):
            pyrosim.Send_Motor_Neuron( name = j + c.numSensorNeurons - 1 , jointName = "Link" + str(j-1) + "_" + "Link" + str(j))

        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                    pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 5 , weight = self.weights[currentRow][currentColumn])

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


            