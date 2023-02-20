import os
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import constants as c
import math



class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
        self.myID = nextAvailableID
        # print(self.weights, "weightssss")
        # exit()


    # def Evaluate(self, DIR_GUI):
    #     self.Create_World() 
    #     self.Create_Body()
    #     self.Create_Brain()
    #     os.system("python3 simulate.py " + str(DIR_GUI) + " " + str(self.myID) + " &")
    #     while not os.path.exists("fitness"+str(self.myID)+".txt"):
    #         time.sleep(0.01)
    #     fitnessFile = open("fitness"+str(self.myID)+".txt", "r")
    #     self.fitness = float(fitnessFile.readline())
    #     print( self.fitness, "lollllol")
    #     fitnessFile.close()

    def Start_Simulation(self, DIR_GUI):
        self.Create_World() 
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + str(DIR_GUI) + " " + str(self.myID) + " &")
        

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        fitnessFile = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(fitnessFile.readline())
        fitnessFile.close()
        # print( self.myID, self.fitness)
        os.system("rm fitness"+str(self.myID)+".txt")
        
       
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x = -30
        y = 10
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        tag = "Cyan"

        r = 0
        g = 0
        b = 1
        a = 1

        linkLenInfo = {}
        linksAdded = []
        connections = []
        self.LinkJointLink = []
        locationMatrix = numpy.zeros((40,40,40,3))

        minX = 0
        minY = 0
        minZ = 0

        maxX = 0
        maxY = 0
        maxZ = 0


        for i in range(0,c.numLinks):
            # length = random.randint(1,2) * numpy.random.rand()
            # width = random.randint(1,2) * numpy.random.rand()
            # height = random.randint(1,2) * numpy.random.rand()

            length = random.randint(1,2) 
            width = random.randint(1,2) 
            height = random.randint(1,2) 

            if (c.randSensorsList[i] == 1):
                b = 0
                g = 1
                tag = "Green"

           
            if (i == 0):
                pyrosim.Send_Cube(name = "Link" + str(i), pos=[length/2,width/2,1] , size=[length,width,2], mass = 1, tag = "rand", color = [1, 0, 0 ,0.4 ] )
                minX = 0
                minY = 0
                minZ = 0
                for x in range(length):
                    for y in range(width):
                        for z in range(height):
                            locationMatrix[20+x,20+y,0+z] = 1
                            maxX = 20+x
                            maxY = 20+y
                            maxZ = 0+z
            else:
                pass
            
            b = 1
            g = 0
            tag = "Cyan"
            flag2 = 1

            if(i == 0):
                linkLenInfo["Link" + str(i)] = [length, width, height,[minX,maxX],[minY,maxY],[minZ,maxZ]]
                
               

                linksAdded.append("Link" + str(i))
               
            else:
                while(flag2 == 1):
                    # jointPositionAxis = random.choice([0, 1, 2])
                    # jointPositionAxis = random.choice([0, 1])
                    jointPositionAxis = 2
                    linkToJoin = random.choice(linksAdded)

                    if ([jointPositionAxis,linkToJoin] in connections):
                        pass
                    else:
                        linkToJoinPointX = linkLenInfo[linkToJoin][3]
                        linkToJoinPointY = linkLenInfo[linkToJoin][4]
                        linkToJoinPointZ = linkLenInfo[linkToJoin][5]

                        MidPointX = (linkToJoinPointX[0]+linkToJoinPointX[1])/2
                        MidPointY = (linkToJoinPointY[0]+linkToJoinPointY[1])/2
                        MidPointZ = (linkToJoinPointZ[0]+linkToJoinPointZ[1])/2

                        tempLocationMatrix = locationMatrix.copy()
                        positionTaken = numpy.array([1,1,1])
                        if jointPositionAxis == 0:
                            for x2 in range(length):
                                for y2 in range(width):
                                    for z2 in range(height):

                                      
                                        if (locationMatrix[math.ceil(x2 + linkToJoinPointX[1]), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] == positionTaken).all():
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()

                                            break
                                        else:
                                            flag2 = 0
                                            minX = linkToJoinPointX[1]
                                            maxX = minX + length
                                            minY = MidPointY - width/2
                                            maxY = minY + width
                                            minZ = MidPointZ - height/2
                                            maxZ = minZ + height
                                            tempLocationMatrix[math.ceil(x2 + linkToJoinPointX[1]), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] = 1

                                      
                        elif jointPositionAxis == 1:
                            for x2 in range(length):
                                for y2 in range(width):
                                    for z2 in range(height):
                                        
                                        if (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(y2 + linkToJoinPointY[1]), math.ceil(MidPointZ - height/2 + z2)] == positionTaken).all():
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()

                                            break
                                        else:
                                            flag2 = 0
                                            minX = MidPointX - length/2
                                            maxX = minX + length
                                            minY = linkToJoinPointY[1]
                                            maxY = minY + width
                                            minZ = MidPointZ - height/2
                                            maxZ = minZ + height
                                            tempLocationMatrix[math.ceil(x2 + linkToJoinPointX[1]), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] = 1

                        else:
                            for x2 in range(length):
                                for y2 in range(width):
                                    for z2 in range(height):
                                        
                                        if (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.ceil(z2 + linkToJoinPointZ[1])] == positionTaken).all():
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            break
                                        else:
                                            flag2 = 0
                                            minX = MidPointX - length/2
                                            maxX = minX + length
                                            minY = MidPointY - width/2
                                            maxY = minY + width
                                            minZ = linkToJoinPointZ[1]
                                            maxZ = minZ + height
                                            tempLocationMatrix[math.ceil(x2 + linkToJoinPointX[1]), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] = 1
                
                locationMatrix = tempLocationMatrix.copy()

                                            
                linkLenInfo["Link" + str(i)] = [length, width, height,[minX,maxX],[minY,maxY],[minZ,maxZ]]
                if (i==1):
                    print(linkLenInfo["Link0"][2], "heightttt")

                linksAdded.append("Link" + str(i))
                connections.append([jointPositionAxis,linkToJoin])  
                print(connections)
                
                
                if (linkToJoin == "Link0"):
                    if (jointPositionAxis == 0):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0], linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]/2], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 1):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1], linkLenInfo[linkToJoin][2]/2], jointAxis = "0 1 0")
                    else:
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]], jointAxis = "0 0 1")
                    
                else:
                    if (jointPositionAxis == 0):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0],0,0], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 1):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [0,linkLenInfo[linkToJoin][1],0], jointAxis = "0 1 0")
                    else:
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0,0,linkLenInfo[linkToJoin][2]], jointAxis = "0 0 1")
                
                if (jointPositionAxis == 0):
                    pyrosim.Send_Cube(name = "Link" +str(i), pos=[length/2,0,0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                elif (jointPositionAxis == 1):
                    pyrosim.Send_Cube(name = "Link" +str(i), pos=[0,width/2,0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                else:
                    pyrosim.Send_Cube(name = "Link" +str(i), pos=[0,0,height/2+1] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])

                self.LinkJointLink.append(linkToJoin + "_" + "Link" + str(i))
                print(self.LinkJointLink)

                


        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        
        counter = 0
        for i in range(0,c.numLinks):
            if (c.randSensorsList[i] == 1):
                pyrosim.Send_Sensor_Neuron(name = counter , linkName = "Link" + str(i))
                counter += 1

        for j in range(1,c.numLinks):
            pyrosim.Send_Motor_Neuron( name = j + c.numSensorNeurons - 1 , jointName = self.LinkJointLink[j-1])

        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                    pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons - 1 , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        # randomRow - three sensor neurons
        randomRow =  random.randint(0,c.numSensorNeurons - 1)
        # randomColumn - two motor neurons
        randomColumn = random.randint(0,c.numMotorNeurons - 1)
        self.weights[randomRow,randomColumn] =  random.random() * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        pass


            