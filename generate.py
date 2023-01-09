import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

for i in range(0,5):
    for j in range(0,5):

        for k in range(0,10):

            pyrosim.Send_Cube(name="Box", pos=[x,y,z+k] , size=[length,width,height])
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9
        y = y+1
        z = 0.5
        length = 1
        width = 1
        height = 1
    y = 0
    x = x+1



# pyrosim.Send_Cube(name="Box2", pos=[x,1,1.5] , size=[length,width,height])


pyrosim.End()
