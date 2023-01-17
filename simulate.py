from simulation import SIMULATION


# # numpy.save("./data/targetAnglesBackLeg.npy", targetAnglesBackLeg)
# # numpy.save("./data/targetAnglesFrontLeg.npy", targetAnglesFrontLeg)
# numpy.save("./data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("./data/frontLegSensorValues.npy", frontLegSensorValues)


simulation = SIMULATION()
simulation.Run()