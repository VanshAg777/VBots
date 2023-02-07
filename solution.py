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
        length = 3
        width = 0.7
        height = 0.4

        pyrosim.Send_Cube(name="Torso", pos=[0,0,3] , size=[length,width,height], mass = 0.1)
        pyrosim.Send_Joint( name = "Torso_FrontLegRight" , parent= "Torso" , child = "FrontLegRight" , type = "revolute", position = [1.05,-0.35,3], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLegRight", pos=[0,-0.15,0] , size=[0.2,0.3,0.1])

        pyrosim.Send_Joint( name = "Torso_FrontLegLeft" , parent= "Torso" , child = "FrontLegLeft" , type = "revolute", position = [1.05,0.35,3], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLegLeft", pos=[0,0.15,0] , size=[0.2,0.3,0.1])

        pyrosim.Send_Joint( name = "Torso_BackLegRight" , parent= "Torso" , child = "BackLegRight" , type = "revolute", position = [-1.05,-0.35,3], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLegRight", pos=[0,-0.15,0] , size=[0.2,0.3,0.1])

        pyrosim.Send_Joint( name = "Torso_BackLegLeft" , parent= "Torso" , child = "BackLegLeft" , type = "revolute", position = [-1.05,0.35,3], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLegLeft", pos=[0,0.15,0] , size=[0.2,0.3,0.1])

        pyrosim.Send_Joint( name = "Torso_LeftWing" , parent= "Torso" , child = "LeftWing" , type = "revolute", position = [0,0.35,3], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftWing", pos=[0,0.1,0] , size=[0.2,0.2,0.1])

        pyrosim.Send_Joint( name = "Torso_RightWing" , parent= "Torso" , child = "RightWing" , type = "revolute", position = [0,-0.35,3], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightWing", pos=[0,-0.1,0] , size=[0.2,0.2,0.1])

        pyrosim.Send_Joint( name = "BackLegLeft_LBLowerLeg" , parent= "BackLegLeft" , child = "LBLowerLeg" , type = "revolute", position = [0,0.3,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LBLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "BackLegRight_RBLowerLeg" , parent= "BackLegRight" , child = "RBLowerLeg" , type = "revolute", position = [0,-0.3,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RBLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "FrontLegRight_RFLowerLeg" , parent= "FrontLegRight" , child = "RFLowerLeg" , type = "revolute", position = [0,-0.3,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RFLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "FrontLegLeft_LFLowerLeg" , parent= "FrontLegLeft" , child = "LFLowerLeg" , type = "revolute", position = [0,0.3,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LFLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "LeftWing_LeftLowerLeg" , parent= "LeftWing" , child = "LeftLowerLeg" , type = "revolute", position = [0,0.1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,1,0.1] , size=[1.5,2,0.1], mass = 0.3)

        pyrosim.Send_Joint( name = "RightWing_RightLowerLeg" , parent= "RightWing" , child = "RightLowerLeg" , type = "revolute", position = [0,-0.1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,-1,0.1] , size=[1.5,2,0.1], mass = 0.3)



        pyrosim.End()


    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "RBLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LBLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RFLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LFLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "RightLowerLeg")


        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_FrontLegRight")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_FrontLegLeft")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_BackLegRight")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLegLeft")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_LeftWing")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_RightWing")

        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "BackLegLeft_LBLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "BackLegRight_RBLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "FrontLegRight_RFLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "FrontLegLeft_LFLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "LeftWing_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "RightWing_RightLowerLeg")



        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )

        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -1.0 )

        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                    pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 6 , weight = self.weights[currentRow][currentColumn])

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


            