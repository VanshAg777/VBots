import numpy 
import random

gravity = -9.8

numpyseed = 776
randomseed = 32
numpy.random.seed(numpyseed)
random.seed(randomseed)

simLength = 7000

amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

# phaseOffsetBackLeg = numpy.pi/7

maxForceBackLeg = 70

amplitudeFrontLeg = numpy.pi/3
frequencyFrontLeg = 10
phaseOffsetFrontLeg = 0

maxForceFrontLeg = 70

numberOfGenerations = 500

populationSize = 10

numLinks = random.randint(2,8)

randSensorsList = [1]
for i in range(0,numLinks-1):
    randSensorsList.append(random.randint(0,1))

numSensorNeurons = randSensorsList.count(1)

numMotorNeurons = numLinks

motorJointRange = 0.2

counter = 0

past = 0

# targetPosition = -(numpy.pi)/4,
# targetPosition = random.uniform(-(numpy.pi)/2,(numpy.pi)/2),