# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy 
# import random
# import constants as c
from simulation import SIMULATION



# physicsClient = p.connect(p.GUI)

# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,c.gravity)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")

# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = numpy.zeros(c.simLength)
# frontLegSensorValues = numpy.zeros(c.simLength)


# targetAnglesBackLeg = c.amplitudeBackLeg * numpy.sin(c.frequencyBackLeg * numpy.linspace(0, 2*(numpy.pi), c.simLength) + c.phaseOffsetBackLeg)

# targetAnglesFrontLeg = c.amplitudeFrontLeg * numpy.sin(c.frequencyFrontLeg * numpy.linspace(0, 2*(numpy.pi), c.simLength) + c.phaseOffsetFrontLeg)

# # numpy.save("./data/targetAnglesBackLeg.npy", targetAnglesBackLeg)
# # numpy.save("./data/targetAnglesFrontLeg.npy", targetAnglesFrontLeg)
# # exit()

# for i in range(0,c.simLength):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotId,
#     jointName = "Torso_BackLeg",
#     controlMode = p.POSITION_CONTROL,
#     targetPosition = targetAnglesBackLeg[i],
#     maxForce = c.maxForceBackLeg)

#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotId,
#     jointName = "Torso_FrontLeg",
#     controlMode = p.POSITION_CONTROL,
#     targetPosition = targetAnglesFrontLeg[i],
#     maxForce = c.maxForceFrontLeg)

#     # backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     # print(backLegTouch)

#     time.sleep( 1/820 )
#     print(i)


# p.disconnect()
# # print(backLegSensorValues)

# numpy.save("./data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("./data/frontLegSensorValues.npy", frontLegSensorValues)
simulation = SIMULATION()