from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)  
        self.Prepare_To_Sense() 
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.Prepare_To_Act()
        
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                print(neuronName)

        for i in self.motors:
            self.motors[i].Set_Value(self.robotId, t)

    def Save_Values(self):
        self.motors.Save_Values()
        self.sensors.Save_Values()
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()


   
      
