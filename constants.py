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

maxForceFrontLeg = 70

numberOfGenerations = 1

populationSize = 1

numSensorNeurons = 4
numMotorNeurons = 8

motorJointRange = 0.5

# targetPosition = -(numpy.pi)/4,
# targetPosition = random.uniform(-(numpy.pi)/2,(numpy.pi)/2),