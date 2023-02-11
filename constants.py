import numpy 
import random

gravity = -9.8

simLength = 10000

amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

# phaseOffsetBackLeg = numpy.pi/7

maxForceBackLeg = 70

amplitudeFrontLeg = numpy.pi/3
frequencyFrontLeg = 10
phaseOffsetFrontLeg = 0

maxForceFrontLeg = 30

numberOfGenerations = 10

populationSize = 10

numLinks = random.randint(3,9)

randSensorsList = []
for i in range(0,numLinks):
    randSensorsList.append(random.randint(0,1))

numSensorNeurons = randSensorsList.count(1)

numMotorNeurons = numLinks

motorJointRange = 0.5

# targetPosition = -(numpy.pi)/4,
# targetPosition = random.uniform(-(numpy.pi)/2,(numpy.pi)/2),