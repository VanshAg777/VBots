import os
import pyrosim_old.pyrosim as pyrosim
import numpy
import random
import time
import constants as c
import pyrosim.pyrosim as new_pyrosim



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

    def Start_Simulation(self, DIR_GUI, x = 0):
        self.Create_World() 
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + str(DIR_GUI) + " " + str(self.myID) + " " + str(x) + " &")
        

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
        # sim = new_pyrosim.Simulator()

        #starts simulation
        # sim.start()
        length = 1
        width = 1
        height = 1
        x = -3
        y = 3
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

        # sim = new_pyrosim.Simulator(play_paused=True)

        # sim.send_cylinder(x=-1)
        # new_pyrosim.Simulator.send_cylinder(x=4, y=4, z=0
        #             #   ,r1=0, r2=0, r3=1,
        #             #   length=1.0, radius=0.1,
        #             #   mass=1.0,
        #             #   collision_group='default',
        #             #   r=1, g=1, b=1,
        #             #   capped=True
        #               )
        pyrosim.End()

    # Original
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

        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])



        pyrosim.End()

    # Prototype (Final Project)
    # def Create_Body(self):
    #     pyrosim.Start_URDF("body.urdf")
    #     length = 1
    #     width = 1
    #     height = 1

    #     pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height])
    #     pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 1 1")
    #     pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])

    #     pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 1 1")
    #     pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

    #     pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "1 1 1")
    #     pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])

    #     pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "1 1 1")
    #     pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

    #     pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "0 1 0")
    #     pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.4,0.4,1])

    #     pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "0 1 0")
    #     pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.4,0.4,1])

    #     pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "1 0 0")
    #     pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.1] , size=[2.4,0.4,0.1])

    #     pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "1 0 0")
    #     pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.1] , size=[2.4,0.4,0.1])



    #     pyrosim.End()


    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")


        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")

        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLeg_RightLowerLeg")



        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )

        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -1.0 )

        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                    pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+4 , weight = self.weights[currentRow][currentColumn])

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


            