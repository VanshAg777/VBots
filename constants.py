import numpy 
import random

gravity = -9.8

simLength = 1000

amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

# phaseOffsetBackLeg = numpy.pi/7

maxForceBackLeg = 22

amplitudeFrontLeg = numpy.pi/3
frequencyFrontLeg = 10
phaseOffsetFrontLeg = 0

maxForceFrontLeg = 22

numberOfGenerations = 10

populationSize = 2

# targetPosition = -(numpy.pi)/4,
# targetPosition = random.uniform(-(numpy.pi)/2,(numpy.pi)/2),