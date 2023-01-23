from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c


class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)

        self.world = WORLD(self.physicsClient)
        self.robot = ROBOT()
          

    def Run(self):
        for t in range(0,c.simLength):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
        
            time.sleep( 1/820 )
            # print(t) 
    
    def __del__(self):
        p.disconnect()
        