import pybullet as p
import pybullet_data
import pyrosim_old.pyrosim as pyrosim

class WORLD:
    def __init__(self, physicsClient):
        self.physicsClient = physicsClient
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
