import pyrosim.pyrosim as pyrosim

def Create_World():

    pyrosim.Start_SDF("world.sdf")
    length = 1
    width = 1
    height = 1
    x = -3
    y = 3
    z = 0.5

    # for i in range(0,5):
    #     for j in range(0,5):
    #         for k in range(0,10):
    #             pyrosim.Send_Cube(name="Box", pos=[x,y,z+k] , size=[length,width,height])
    #             length = length * 0.9
    #             width = width * 0.9
    #             height = height * 0.9
    #         y = y+1
    #         z = 0.5
    #         length = 1
    #         width = 1
    #         height = 1
    #     y = 0
    #     x = x+1

    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    # pyrosim.Send_Cube(name="Box2", pos=[x,1,1.5] , size=[length,width,height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    length = 1
    width = 1
    height = 1
    x = 0
    y = 0
    z = 0.5

    # slide bot
    # pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length,width,height])
    # pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    # pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5] , size=[length,width,height])

    # pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
    # pyrosim.Send_Cube(name="Link2", pos=[0,0,0.5] , size=[length,width,height])

    # pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,0.5,0.5])
    # pyrosim.Send_Cube(name="Link3", pos=[0,0.5,0] , size=[length,width,height])


    pyrosim.Send_Cube(name="Torso", pos=[1.5,y,1.5] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[length,width,height])

    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[length,width,height])
    pyrosim.End()




Create_World()
Create_Robot()