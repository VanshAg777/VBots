import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy 
import random


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

# targetAngles = numpy.sin(numpy.linspace(0, 2*(numpy.pi), 1000))
# targetAngles = ((targetAngles/(2))*(numpy.pi/2))
# numpy.save("./data/targetAngles.npy", targetAngles)
# print(targetAngles)

amplitudeBackLeg = numpy.pi/3
frequencyBackLeg = 10
phaseOffsetBackLeg = numpy.pi/7

targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(frequencyBackLeg * numpy.linspace(0, 2*(numpy.pi), 1000) + phaseOffsetBackLeg)


amplitudeFrontLeg = numpy.pi/3
frequencyFrontLeg = 10
phaseOffsetFrontLeg = 0

targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * numpy.linspace(0, 2*(numpy.pi), 1000) + phaseOffsetFrontLeg)

# numpy.save("./data/targetAnglesBackLeg.npy", targetAnglesBackLeg)
# numpy.save("./data/targetAnglesFrontLeg.npy", targetAnglesFrontLeg)
# exit()

for i in range(0,1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    # targetPosition = -(numpy.pi)/4,
    # targetPosition = random.uniform(-(numpy.pi)/2,(numpy.pi)/2),
    targetPosition = targetAnglesBackLeg[i],
    maxForce = 22)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = targetAnglesFrontLeg[i],
    maxForce = 22)

    # backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    # print(backLegTouch)
    time.sleep( 1/820 )
    print(i)


p.disconnect()
# print(backLegSensorValues)

numpy.save("./data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("./data/frontLegSensorValues.npy", frontLegSensorValues)
