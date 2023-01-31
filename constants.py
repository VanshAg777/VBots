import numpy 
import random

gravity = -9.8

simLength = 1000

amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

# phaseOffsetBackLeg = numpy.pi/7

maxForceBackLeg = 23

amplitudeFrontLeg = numpy.pi/3
frequencyFrontLeg = 10
phaseOffsetFrontLeg = 0

maxForceFrontLeg = 23

numberOfGenerations = 10

populationSize = 10

numSensorNeurons = 4
numMotorNeurons = 8

motorJointRange = 0.8

# targetPosition = -(numpy.pi)/4,
# targetPosition = random.uniform(-(numpy.pi)/2,(numpy.pi)/2),