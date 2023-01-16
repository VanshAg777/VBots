import numpy
import matplotlib.pyplot


backLegSensorValues = numpy.load("./data/backLegSensorValues.npy")
print(backLegSensorValues)


frontLegSensorValues =  numpy.load("./data/frontLegSensorValues.npy") 


matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg')
matplotlib.pyplot.legend()


matplotlib.pyplot.show()