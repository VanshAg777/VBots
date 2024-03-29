import os
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import constants as c
import math
from collections import Counter
numpy.random.seed(c.numpyseed)
random.seed(c.randomseed)



class SOLUTION:
    def __init__(self, nextAvailableID):
        self.max_links = 9
        self.weights = numpy.random.rand(self.max_links+2,self.max_links+2) * 2 - 1
        self.myID = nextAvailableID
        self.linkLenInfo = []
        self.grandConnections = {}
        self.randSensorsList =[]
        self.linksAdded = []
        self.locationMatrix = numpy.zeros((40,40,40))
        self.connections = []
       


    

    def Start_Simulation(self, DIR_GUI, child_true = 0):
        if (self.myID == 0):
            self.Create_World()
        if (child_true == 1):
            self.Create_Child_Body()
            self.Create_Child_Brain()
        else:
            self.Create_Body()
            self.Create_Brain()
        os.system("python3 simulate.py " + str(DIR_GUI) + " " + str(self.myID) + " &")
        

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        fitnessFile = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(fitnessFile.readline())
        fitnessFile.close()
        os.system("rm fitness"+str(self.myID)+".txt")
        return(self.fitness)
        
       
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

    def Create_Child_Body(self):
        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")

        tag = "Cyan"

        r = 0
        g = 0
        b = 1
        a = 1
        linkLenInfo = self.linkLenInfo
        grandConnections =  self.grandConnections

        randSensorsList = self.randSensorsList
        linksAdded = self.linksAdded
        LinkJoitLink = grandConnections.keys()

        counter = 0

        for link in linksAdded:
            length = linkLenInfo[link][0]
            width = linkLenInfo[link][1]
            height = linkLenInfo[link][2]
            if (randSensorsList[counter] == 1):
                b = 0
                g = 1
                tag = "Green"
            if (link == "Link0"):
                pyrosim.Send_Cube(name = link, pos=[length/2,width/2,height/2] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ] )
                counter += 1
            else:
                for j in LinkJoitLink:
                    if ("_" + link) in j:
                        jointPositionAxis = grandConnections[j]
                        linkToJoin = j[0:j.find("_")]
                        break

                for k in LinkJoitLink:
                    if ("_" + linkToJoin) in k:
                        grandParAxis = grandConnections[k]

               
                if (linkToJoin == "Link0"):
                    if (jointPositionAxis == 0):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0], linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]/2], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 1):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1], linkLenInfo[linkToJoin][2]/2], jointAxis = "0 1 0")
                    elif (jointPositionAxis == 2):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]], jointAxis = "0 0 1")
                    elif (jointPositionAxis == 3):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]/2], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 4):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 1 0")
                    else:                        
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "0 1 0")


                elif(grandParAxis == jointPositionAxis):
                    if (jointPositionAxis == 0):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0],0,0], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 1):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [0,linkLenInfo[linkToJoin][1],0], jointAxis = "0 1 0")
                    elif (jointPositionAxis == 2):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0,0,linkLenInfo[linkToJoin][2]], jointAxis = "0 0 1")
                    elif (jointPositionAxis == 3):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]),0,0], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 4):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [0,-(linkLenInfo[linkToJoin][1]),0], jointAxis = "0 1 0")
                    else:
                        pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0,0,-(linkLenInfo[linkToJoin][2])], jointAxis = "0 0 1")
                    


                else:
                    if (grandParAxis == 0):
                        if (jointPositionAxis == 1):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 2):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 0 1")
                        elif (jointPositionAxis == 4):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, -(linkLenInfo[linkToJoin][1]/2), 0], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 5):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0, -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 0 1")
                        
                    elif (grandParAxis == 1):
                        if (jointPositionAxis == 0):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 2):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 0 1")
                        elif (jointPositionAxis == 3):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 5):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 0 1")
                    
                    
                    elif (grandParAxis == 2):
                        if (jointPositionAxis == 0):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0,  linkLenInfo[linkToJoin][2]/2], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 1):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 3):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), 0,  linkLenInfo[linkToJoin][2]/2], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 4):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0, -(linkLenInfo[linkToJoin][1]/2), linkLenInfo[linkToJoin][2]/2], jointAxis = "0 1 0")
                        
                    # Negative Grand Axises
                    elif (grandParAxis == 3):
                        if (jointPositionAxis == 1):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 2):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), 0, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 0 1")
                        elif (jointPositionAxis == 4):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), -(linkLenInfo[linkToJoin][1]/2), 0], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 5):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), 0, -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 0 1")
                        
                    elif (grandParAxis == 4):
                        if (jointPositionAxis == 0):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, -(linkLenInfo[linkToJoin][1]/2), 0], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 2):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0, -(linkLenInfo[linkToJoin][1]/2), linkLenInfo[linkToJoin][2]/2], jointAxis = "0 0 1")
                        elif (jointPositionAxis == 3):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), -(linkLenInfo[linkToJoin][1]/2), 0], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 5):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0, -(linkLenInfo[linkToJoin][1]/2), -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 0 1")
                    
                    else:
                        if (jointPositionAxis == 0):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin , child = link , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0,  -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 1):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 3):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link, parent = linkToJoin , child = link , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), 0,  -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 4):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + link , parent = linkToJoin  , child = link , type = "revolute", position = [0, -(linkLenInfo[linkToJoin][1]/2), -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 1 0")
                        

                if (jointPositionAxis == 0):
                    pyrosim.Send_Cube(name = link, pos=[length/2,0,0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                elif (jointPositionAxis == 1):
                    pyrosim.Send_Cube(name = link, pos=[0,width/2,0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                elif (jointPositionAxis == 2):
                    pyrosim.Send_Cube(name = link, pos=[0,0,height/2] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                # Negative Axis Links
                elif (jointPositionAxis == 3):
                    pyrosim.Send_Cube(name = link, pos=[-(length/2),0,0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                elif (jointPositionAxis == 4):
                    pyrosim.Send_Cube(name = link, pos=[0,-(width/2),0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                else:
                    pyrosim.Send_Cube(name = link, pos=[0,0,-(height/2)] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                
                b = 1
                g = 0
                tag = "Cyan"
                counter += 1
                # flag2 = 1

        self.linkLenInfo = linkLenInfo
        self.grandConnections = grandConnections
        self.randSensorsList = randSensorsList
        self.linksAdded = linksAdded
        pyrosim.End()
                    


    def Create_Body(self):
        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
        # pyrosim.Start_URDF("body.urdf")

        tag = "Cyan"

        r = 0
        g = 0
        b = 1
        a = 1

        linkLenInfo = {}
        linksAdded = []
        connections = []
        grandConnections = {}
        self.LinkJointLink = []
        locationMatrix = self.locationMatrix.copy()

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
                pyrosim.Send_Cube(name = "Link" + str(i), pos=[length/2,width/2,height/2] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ] )
                minX = 20
                minY = 20
                minZ = 0
                for x in range(length):
                    for y in range(width):
                        for z in range(height):
                            locationMatrix[20+x,20+y,0+z] = 1
                            maxX = 20+x+1
                            maxY = 20+y+1
                            maxZ = 0+z+1
            else:
                pass

            if(i == 0):
                linkLenInfo["Link" + str(i)] = [length, width, height,[minX,maxX],[minY,maxY],[minZ,maxZ]]
                linksAdded.append("Link" + str(i))
                result = numpy.where(numpy.logical_and(locationMatrix>0, locationMatrix<2))
                
                b = 1
                g = 0
                tag = "Cyan"
                flag2 = 1
               
            else:
                while(flag2 == 1):
                    jointPositionAxis = random.choice([0, 1, 2, 3, 4, 5])
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

                        inner_flag1 = 0
                        inner_flag2 = 0
                        
                        if jointPositionAxis == 0:
                            minX = linkToJoinPointX[1]
                            maxX = minX + length
                            minY = MidPointY - width/2
                            maxY = minY + width
                            minZ = MidPointZ - height/2
                            maxZ = minZ + height
                            if (minX < 0) or (minY < 0) or (minZ < 0):
                                flag2 = 1
                                tempLocationMatrix = locationMatrix.copy()
                                length = random.randint(1,2) 
                                width = random.randint(1,2) 
                                height = random.randint(1,2) 
                                inner_flag1 = 1

                            for x2 in range(math.ceil(maxX) - math.floor(minX)):
                                for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                    for z2 in range(math.ceil(maxZ) - math.floor(minZ)):

                                        if (x2 == 0) or (y2 == 0) or (z2 == 0):

                                            if (locationMatrix[math.floor(x2 + linkToJoinPointX[1]), math.floor(MidPointY - width/2 + y2), math.floor(MidPointZ - height/2 + z2)] == 1):           
                                                flag2 = 1
                                                tempLocationMatrix = locationMatrix.copy()
                                                inner_flag1 = 1
                                                break
                                            else:
                                                flag2 = 0
                                            
                                                tempLocationMatrix[math.floor(x2 + linkToJoinPointX[1]), math.floor(MidPointY - width/2 + y2), math.floor(MidPointZ - height/2 + z2)] = 1
                                        



                                        # if (locationMatrix[math.ceil(x2 + linkToJoinPointX[1]), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] == positionTaken).all():
                                        elif (locationMatrix[math.ceil(x2 + linkToJoinPointX[1]), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] == 1):           
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break

                                        else:
                                            flag2 = 0
                                        
                                            tempLocationMatrix[math.ceil(x2 + linkToJoinPointX[1]), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] = 1

                                        if inner_flag1 == 1:
                                            inner_flag2 = 1
                                            flag2 = 1
                                            break
                                    if inner_flag2 == 1:
                                            break
                                      
                        elif jointPositionAxis == 1:
                            minX = MidPointX - length/2
                            maxX = minX + length
                            minY = linkToJoinPointY[1]
                            maxY = minY + width
                            minZ = MidPointZ - height/2
                            maxZ = minZ + height
                            if (minX < 0) or (minY < 0) or (minZ < 0):
                                flag2 = 1
                                tempLocationMatrix = locationMatrix.copy()
                                length = random.randint(1,2) 
                                width = random.randint(1,2) 
                                height = random.randint(1,2) 
                                inner_flag1 = 1

                            for x2 in range(math.ceil(maxX) - math.floor(minX)):
                                for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                    for z2 in range(math.ceil(maxZ) - math.floor(minZ)):
                                        
                                        if (x2 == 0) or (y2 == 0) or (z2 == 0):

                                            if (locationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(y2 + linkToJoinPointY[1]), math.floor(MidPointZ - height/2 + z2)] == 1):
                                                flag2 = 1
                                                tempLocationMatrix = locationMatrix.copy()
                                                inner_flag1 = 1
                                                break

                                            else:
                                                flag2 = 0
                                               
                                                tempLocationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(y2 + linkToJoinPointY[1]), math.floor(MidPointZ - height/2 + z2)] = 1


                                        # if (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(y2 + linkToJoinPointY[1]), math.ceil(MidPointZ - height/2 + z2)] == positionTaken).all():
                                        elif (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(y2 + linkToJoinPointY[1]), math.ceil(MidPointZ - height/2 + z2)] == 1):
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break

                                        else:
                                            flag2 = 0
                                        
                                            tempLocationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(y2 + linkToJoinPointY[1]), math.ceil(MidPointZ - height/2 + z2)] = 1
                                        if inner_flag1 == 1:
                                            inner_flag2 = 1
                                            flag2 = 1
                                            break
                                    if inner_flag2 == 1:
                                            break

                        elif jointPositionAxis == 2:
                            minX = MidPointX - length/2
                            maxX = minX + length
                            minY = MidPointY - width/2
                            maxY = minY + width
                            minZ = linkToJoinPointZ[1]
                            maxZ = minZ + height
                            if (minX < 0) or (minY < 0) or (minZ < 0):
                                flag2 = 1
                                tempLocationMatrix = locationMatrix.copy()
                                length = random.randint(1,2) 
                                width = random.randint(1,2) 
                                height = random.randint(1,2) 
                                inner_flag1 = 1

                            for x2 in range(math.ceil(maxX) - math.floor(minX)):
                                for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                    for z2 in range(math.ceil(maxZ) - math.floor(minZ)):
                                        
                                        if (x2 == 0) or (y2 == 0) or (z2 == 0):
                                            if (locationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(MidPointY - width/2 + y2), math.floor(z2 + linkToJoinPointZ[1])] == 1):                                            
                                                flag2 = 1
                                                tempLocationMatrix = locationMatrix.copy()
                                                inner_flag1 = 1
                                                break

                                            else:
                                                flag2 = 0
                                                
                                                tempLocationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(MidPointY - width/2 + y2), math.floor(z2 + linkToJoinPointZ[1])] = 1
                

                                        # if (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.ceil(z2 + linkToJoinPointZ[1])] == positionTaken).all():
                                        elif (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.ceil(z2 + linkToJoinPointZ[1])] == 1):                                            
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break
                                        else:
                                            flag2 = 0
                                        
                                            tempLocationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.ceil(z2 + linkToJoinPointZ[1])] = 1
                                        if inner_flag1 == 1:
                                            inner_flag2 = 1
                                            flag2 = 1
                                            break
                                    if inner_flag2 == 1:
                                            break

                        # Negative Axis
                        elif jointPositionAxis == 3:
                           
                            maxX = linkToJoinPointX[0]
                            minX = maxX - length
                            minY = MidPointY - width/2
                            maxY = minY + width
                            minZ = MidPointZ - height/2
                            maxZ = minZ + height
                            if (minX < 0) or (minY < 0) or (minZ < 0):
                                flag2 = 1
                                tempLocationMatrix = locationMatrix.copy()
                                length = random.randint(1,2) 
                                width = random.randint(1,2) 
                                height = random.randint(1,2)  
                                inner_flag1 = 1

                            for x2 in range(1,math.floor(maxX) - math.floor(minX)+1):
                                for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                    for z2 in range(math.ceil(maxZ) - math.floor(minZ)):

                                        if (x2 == 0) or (y2 == 0) or (z2 == 0):

                                            if (locationMatrix[math.floor(linkToJoinPointX[0] - x2), math.floor(MidPointY - width/2 + y2), math.floor(MidPointZ - height/2 + z2)] == 1):           
                                                flag2 = 1
                                                tempLocationMatrix = locationMatrix.copy()
                                                inner_flag1 = 1

                                                
                                                break
                                            else:
                                                flag2 = 0
                                                tempLocationMatrix[math.floor(linkToJoinPointX[0] - x2), math.floor(MidPointY - width/2 + y2), math.floor(MidPointZ - height/2 + z2)] = 1


                                        elif (locationMatrix[math.floor(linkToJoinPointX[0] - x2), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] == 1):           
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break

                                        else:
                                            flag2 = 0
                                            tempLocationMatrix[math.floor(linkToJoinPointX[0] - x2), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] = 1
                                        if inner_flag1 == 1:
                                            inner_flag2 = 1
                                            flag2 = 1
                                            break
                                    if inner_flag2 == 1:
                                            break
                                      
                        elif jointPositionAxis == 4:
                            minX = MidPointX - length/2
                            maxX = minX + length
                            maxY = linkToJoinPointY[0]
                            minY = maxY - width
                            minZ = MidPointZ - height/2
                            maxZ = minZ + height

                            if (minX < 0) or (minY < 0) or (minZ < 0):
                                flag2 = 1
                                tempLocationMatrix = locationMatrix.copy()
                                length = random.randint(1,2) 
                                width = random.randint(1,2) 
                                height = random.randint(1,2) 
                                inner_flag1 = 1

                            for x2 in range(math.ceil(maxX) - math.floor(minX)):
                                for y2 in range(1,math.floor(maxY) - math.floor(minY)+1):
                                    for z2 in range(math.ceil(maxZ) - math.floor(minZ)):
                                        
                                        if (x2 == 0) or (y2 == 0) or (z2 == 0):

                                            if (locationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(linkToJoinPointY[0] - y2), math.floor(MidPointZ - height/2 + z2)] == 1):
                                                flag2 = 1
                                                tempLocationMatrix = locationMatrix.copy()
                                                inner_flag1 = 1
                                                break

                                            else:
                                                flag2 = 0
                                                tempLocationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(linkToJoinPointY[0] - y2), math.floor(MidPointZ - height/2 + z2)] = 1


                                        elif (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.floor(linkToJoinPointY[0] - y2), math.ceil(MidPointZ - height/2 + z2)] == 1):
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break

                                        else:
                                            flag2 = 0
                                            tempLocationMatrix[math.ceil(MidPointX - length/2 + x2), math.floor(linkToJoinPointY[0] - y2), math.ceil(MidPointZ - height/2 + z2)] = 1
                                        if inner_flag1 == 1:
                                            inner_flag2 = 1
                                            flag2 = 1
                                            break
                                    if inner_flag2 == 1:
                                            break

                        else:
                            minX = MidPointX - length/2
                            maxX = minX + length
                            minY = MidPointY - width/2
                            maxY = minY + width
                            maxZ = linkToJoinPointZ[0]
                            minZ = maxZ - height
                            if (minX < 0) or (minY < 0) or (minZ < 0):
                                flag2 = 1
                                tempLocationMatrix = locationMatrix.copy()
                                length = random.randint(1,2) 
                                width = random.randint(1,2) 
                                height = random.randint(1,2) 
                                inner_flag1 = 1
                                
                            for x2 in range(math.ceil(maxX) - math.floor(minX)):
                                for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                    for z2 in range(1,math.floor(maxZ) - math.floor(minZ)+1):
                                        
                                        if (x2 == 0) or (y2 == 0) or (z2 == 0):
                                            if (locationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(MidPointY - width/2 + y2), math.floor(linkToJoinPointZ[1] - z2)] == 1):                                            
                                                flag2 = 1
                                                tempLocationMatrix = locationMatrix.copy()
                                                inner_flag1 = 1
                                                break

                                            else:
                                                flag2 = 0
                                               
                                                tempLocationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(MidPointY - width/2 + y2), math.floor(linkToJoinPointZ[1] - z2)] = 1
                

                                        # if (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.ceil(z2 + linkToJoinPointZ[1])] == positionTaken).all():
                                        elif (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.floor(linkToJoinPointZ[1] - z2)] == 1):                                            
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break
                                        else:
                                            flag2 = 0
                                        
                                            tempLocationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.floor(linkToJoinPointZ[1] - z2)] = 1
                                        if inner_flag1 == 1:
                                            inner_flag2 = 1
                                            flag2 = 1
                                            break
                                    if inner_flag2 == 1:
                                            break


                locationMatrix = tempLocationMatrix.copy()
                result = numpy.where(numpy.logical_and(locationMatrix>0, locationMatrix<2))

                                            
                linkLenInfo["Link" + str(i)] = [length, width, height,[minX,maxX],[minY,maxY],[minZ,maxZ]]

                linksAdded.append("Link" + str(i))
                connections.append([jointPositionAxis,linkToJoin])  
                grandConnections[linkToJoin+"_"+"Link"+ str(i)] = jointPositionAxis
                self.connections = connections
             
                for li in reversed(range(len(self.LinkJointLink))) :
                    if ("_"+linkToJoin) in self.LinkJointLink[li]:
                        grandparentLink = self.LinkJointLink[li]
                        grandParAxis = grandConnections[grandparentLink]
                        break
                
                
                if (linkToJoin == "Link0"):
                    if (jointPositionAxis == 0):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0], linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]/2], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 1):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1], linkLenInfo[linkToJoin][2]/2], jointAxis = "0 1 0")
                    elif (jointPositionAxis == 2):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]], jointAxis = "0 0 1")
                    elif (jointPositionAxis == 3):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]/2], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 4):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 1 0")
                    else:
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "0 1 0")



                elif(grandParAxis == jointPositionAxis):
                    if (jointPositionAxis == 0):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0],0,0], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 1):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [0,linkLenInfo[linkToJoin][1],0], jointAxis = "0 1 0")
                    elif (jointPositionAxis == 2):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0,0,linkLenInfo[linkToJoin][2]], jointAxis = "0 0 1")
                    elif (jointPositionAxis == 3):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]),0,0], jointAxis = "1 0 0")
                    elif (jointPositionAxis == 4):
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [0,-(linkLenInfo[linkToJoin][1]),0], jointAxis = "0 1 0")
                    else:
                        pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0,0,-(linkLenInfo[linkToJoin][2])], jointAxis = "0 0 1")
                    


                else:
                    if (grandParAxis == 0):
                        if (jointPositionAxis == 1):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 2):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 0 1")
                        elif (jointPositionAxis == 4):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, -(linkLenInfo[linkToJoin][1]/2), 0], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 5):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0, -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 0 1")
                        
                    elif (grandParAxis == 1):
                        if (jointPositionAxis == 0):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 2):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 0 1")
                        elif (jointPositionAxis == 3):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 5):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 0 1")
                    
                    
                    elif (grandParAxis == 2):
                        if (jointPositionAxis == 0):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0,  linkLenInfo[linkToJoin][2]/2], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 1):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 3):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), 0,  linkLenInfo[linkToJoin][2]/2], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 4):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0, -(linkLenInfo[linkToJoin][1]/2), linkLenInfo[linkToJoin][2]/2], jointAxis = "0 1 0")
                        
                    # Negative Grand Axises
                    elif (grandParAxis == 3):
                        if (jointPositionAxis == 1):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), linkLenInfo[linkToJoin][1]/2, 0], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 2):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), 0, linkLenInfo[linkToJoin][2]/2], jointAxis = "0 0 1")
                        elif (jointPositionAxis == 4):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), -(linkLenInfo[linkToJoin][1]/2), 0], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 5):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), 0, -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 0 1")
                        
                    elif (grandParAxis == 4):
                        if (jointPositionAxis == 0):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, -(linkLenInfo[linkToJoin][1]/2), 0], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 2):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0, -(linkLenInfo[linkToJoin][1]/2), linkLenInfo[linkToJoin][2]/2], jointAxis = "0 0 1")
                        elif (jointPositionAxis == 3):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), -(linkLenInfo[linkToJoin][1]/2), 0], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 5):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0, -(linkLenInfo[linkToJoin][1]/2), -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 0 1")
                    
                    else:
                        if (jointPositionAxis == 0):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [linkLenInfo[linkToJoin][0]/2, 0,  -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 1):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0, linkLenInfo[linkToJoin][1]/2, -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 1 0")
                        elif (jointPositionAxis == 3):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin , child = "Link" + str(i) , type = "revolute", position = [-(linkLenInfo[linkToJoin][0]/2), 0,  -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "1 0 0")
                        elif (jointPositionAxis == 4):
                            pyrosim.Send_Joint(name = linkToJoin + "_" + "Link" + str(i) , parent = linkToJoin  , child = "Link" + str(i) , type = "revolute", position = [0, -(linkLenInfo[linkToJoin][1]/2), -(linkLenInfo[linkToJoin][2]/2)], jointAxis = "0 1 0")
                        

                if (jointPositionAxis == 0):
                    pyrosim.Send_Cube(name = "Link" +str(i), pos=[length/2,0,0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                elif (jointPositionAxis == 1):
                    pyrosim.Send_Cube(name = "Link" +str(i), pos=[0,width/2,0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                elif (jointPositionAxis == 2):
                    pyrosim.Send_Cube(name = "Link" +str(i), pos=[0,0,height/2] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                # Negative Axis Links
                elif (jointPositionAxis == 3):
                    pyrosim.Send_Cube(name = "Link" +str(i), pos=[-(length/2),0,0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                elif (jointPositionAxis == 4):
                    pyrosim.Send_Cube(name = "Link" +str(i), pos=[0,-(width/2),0] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                else:
                    pyrosim.Send_Cube(name = "Link" +str(i), pos=[0,0,-(height/2)] , size=[length,width,height], mass = 1, tag = tag, color = [r, g, b ,a ])
                self.LinkJointLink.append(linkToJoin + "_" + "Link" + str(i))
                b = 1
                g = 0
                tag = "Cyan"
                flag2 = 1
                
        self.locationMatrix = locationMatrix.copy()
        self.linkLenInfo = linkLenInfo
        self.grandConnections = grandConnections
        self.randSensorsList = c.randSensorsList
        self.linksAdded = linksAdded

        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        
        counter = 0
        for i in range(0,c.numLinks):
            if (c.randSensorsList[i] == 1):
                pyrosim.Send_Sensor_Neuron(name = counter , linkName = "Link" + str(i))
                counter += 1

        for j in range(0,c.numLinks - 1):
            pyrosim.Send_Motor_Neuron( name = j + c.numSensorNeurons  , jointName = self.LinkJointLink[j])

        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                    pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons - 1 , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Create_Child_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        counter = 0
        numLinks = len(self.linksAdded)
        for i in range(0,numLinks):
            if (self.randSensorsList[i] == 1):
                pyrosim.Send_Sensor_Neuron(name = counter , linkName = self.linksAdded[i])
                counter += 1
        LinkJointLink = self.grandConnections.keys()
        listLJL = list(LinkJointLink)
        numSensorNeurons = self.randSensorsList.count(1)
        for j in range(0,numLinks - 1):
            pyrosim.Send_Motor_Neuron( name = j + numSensorNeurons  , jointName = listLJL[j])
        
        for currentRow in range(0,numSensorNeurons):
            for currentColumn in range(0,numLinks-1):
                    pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + numSensorNeurons , weight = self.weights[currentRow][currentColumn])
                   
        pyrosim.End()


    def Mutate(self):
        linkLenInfo = self.linkLenInfo
        grandConnections =  self.grandConnections
        randSensorsList = self.randSensorsList
        linksAdded = self.linksAdded
        LinkJoitLink = grandConnections.keys()
        LinkJoiNtLink = list(LinkJoitLink)
        locationMatrix = self.locationMatrix.copy()
        connections = self.connections

        # 0 - Remove Link/ 1 - Add Link/ 2 - None
        add_remove_none = 2
        if len(LinkJoiNtLink) > 3 and len(LinkJoiNtLink) < self.max_links:
            add_remove_none = random.choice([0, 1, 2])
            # add_remove_none = 0
        elif len(LinkJoiNtLink) > 3 and len(LinkJoiNtLink) >= self.max_links:
            add_remove_none = random.choice([0, 2])
        elif len(LinkJoiNtLink) < 3:
            add_remove_none = random.choice([1, 2])



        # Remove Link
      
        if (add_remove_none == 0):
            LinksWithChild = []
            for li in linksAdded:
                for j in LinkJoiNtLink:
                        if (li + "_" ) in j:
                            LinksWithChild.append(li)
            childlessLinks = list((Counter(linksAdded)-Counter(LinksWithChild)).elements())
            linkToRemove = random.choice(childlessLinks)
            linksAdded.remove(linkToRemove)
            del linkLenInfo[linkToRemove]
            randSensorsList.pop()

            for lj in LinkJoiNtLink:
                if("_" + linkToRemove) in lj:
                    LinkJoitLinkToRemove = lj
                    break

           
            del grandConnections[LinkJoitLinkToRemove]
           



        elif(add_remove_none == 1):
            length = random.randint(1,2) 
            width = random.randint(1,2) 
            height = random.randint(1,2) 
            flag2 = 1
            while(flag2 == 1):
                jointPositionAxis = random.choice([0, 1, 2, 3, 4, 5])
                
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

                    inner_flag1 = 0
                    inner_flag2 = 0
                    
                    if jointPositionAxis == 0:
                        minX = linkToJoinPointX[1]
                        maxX = minX + length
                        minY = MidPointY - width/2
                        maxY = minY + width
                        minZ = MidPointZ - height/2
                        maxZ = minZ + height
                        if (minX < 0) or (minY < 0) or (minZ < 0):
                            flag2 = 1
                            tempLocationMatrix = locationMatrix.copy()
                            length = random.randint(1,2) 
                            width = random.randint(1,2) 
                            height = random.randint(1,2) 
                            inner_flag1 = 1

                        for x2 in range(math.ceil(maxX) - math.floor(minX)):
                            for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                for z2 in range(math.ceil(maxZ) - math.floor(minZ)):

                                    if (x2 == 0) or (y2 == 0) or (z2 == 0):

                                        if (locationMatrix[math.floor(x2 + linkToJoinPointX[1]), math.floor(MidPointY - width/2 + y2), math.floor(MidPointZ - height/2 + z2)] == 1):           
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break
                                        else:
                                            flag2 = 0
                                        
                                            tempLocationMatrix[math.floor(x2 + linkToJoinPointX[1]), math.floor(MidPointY - width/2 + y2), math.floor(MidPointZ - height/2 + z2)] = 1
                                    



                                    elif (locationMatrix[math.ceil(x2 + linkToJoinPointX[1]), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] == 1):           
                                        flag2 = 1
                                        tempLocationMatrix = locationMatrix.copy()
                                        inner_flag1 = 1
                                        break

                                    else:
                                        flag2 = 0
                                    
                                        tempLocationMatrix[math.ceil(x2 + linkToJoinPointX[1]), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] = 1

                                    if inner_flag1 == 1:
                                        inner_flag2 = 1
                                        flag2 = 1
                                        break
                                if inner_flag2 == 1:
                                        break
                                    
                    elif jointPositionAxis == 1:
                        minX = MidPointX - length/2
                        maxX = minX + length
                        minY = linkToJoinPointY[1]
                        maxY = minY + width
                        minZ = MidPointZ - height/2
                        maxZ = minZ + height
                        if (minX < 0) or (minY < 0) or (minZ < 0):
                            flag2 = 1
                            tempLocationMatrix = locationMatrix.copy()
                            length = random.randint(1,2) 
                            width = random.randint(1,2) 
                            height = random.randint(1,2) 
                            inner_flag1 = 1

                        for x2 in range(math.ceil(maxX) - math.floor(minX)):
                            for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                for z2 in range(math.ceil(maxZ) - math.floor(minZ)):
                                    
                                    if (x2 == 0) or (y2 == 0) or (z2 == 0):

                                        if (locationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(y2 + linkToJoinPointY[1]), math.floor(MidPointZ - height/2 + z2)] == 1):
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break

                                        else:
                                            flag2 = 0
                                            
                                            tempLocationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(y2 + linkToJoinPointY[1]), math.floor(MidPointZ - height/2 + z2)] = 1


                                    # if (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(y2 + linkToJoinPointY[1]), math.ceil(MidPointZ - height/2 + z2)] == positionTaken).all():
                                    elif (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(y2 + linkToJoinPointY[1]), math.ceil(MidPointZ - height/2 + z2)] == 1):
                                        flag2 = 1
                                        tempLocationMatrix = locationMatrix.copy()
                                        inner_flag1 = 1
                                        break

                                    else:
                                        flag2 = 0
                                    
                                        tempLocationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(y2 + linkToJoinPointY[1]), math.ceil(MidPointZ - height/2 + z2)] = 1
                                    if inner_flag1 == 1:
                                        inner_flag2 = 1
                                        flag2 = 1
                                        break
                                if inner_flag2 == 1:
                                        break

                    elif jointPositionAxis == 2:
                        minX = MidPointX - length/2
                        maxX = minX + length
                        minY = MidPointY - width/2
                        maxY = minY + width
                        minZ = linkToJoinPointZ[1]
                        maxZ = minZ + height
                        if (minX < 0) or (minY < 0) or (minZ < 0):
                            flag2 = 1
                            tempLocationMatrix = locationMatrix.copy()
                            length = random.randint(1,2) 
                            width = random.randint(1,2) 
                            height = random.randint(1,2) 
                            inner_flag1 = 1

                        for x2 in range(math.ceil(maxX) - math.floor(minX)):
                            for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                for z2 in range(math.ceil(maxZ) - math.floor(minZ)):
                                    
                                    if (x2 == 0) or (y2 == 0) or (z2 == 0):
                                        if (locationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(MidPointY - width/2 + y2), math.floor(z2 + linkToJoinPointZ[1])] == 1):                                            
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break

                                        else:
                                            flag2 = 0
                                            
                                            tempLocationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(MidPointY - width/2 + y2), math.floor(z2 + linkToJoinPointZ[1])] = 1
            

                                    # if (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.ceil(z2 + linkToJoinPointZ[1])] == positionTaken).all():
                                    elif (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.ceil(z2 + linkToJoinPointZ[1])] == 1):                                            
                                        flag2 = 1
                                        tempLocationMatrix = locationMatrix.copy()
                                        inner_flag1 = 1
                                        break
                                    else:
                                        flag2 = 0
                                    
                                        tempLocationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.ceil(z2 + linkToJoinPointZ[1])] = 1
                                    if inner_flag1 == 1:
                                        inner_flag2 = 1
                                        flag2 = 1
                                        break
                                if inner_flag2 == 1:
                                        break

                    # Negative Axis
                    elif jointPositionAxis == 3:
                        
                        maxX = linkToJoinPointX[0]
                        minX = maxX - length
                        minY = MidPointY - width/2
                        maxY = minY + width
                        minZ = MidPointZ - height/2
                        maxZ = minZ + height
                        if (minX < 0) or (minY < 0) or (minZ < 0):
                            flag2 = 1
                            tempLocationMatrix = locationMatrix.copy()
                            length = random.randint(1,2) 
                            width = random.randint(1,2) 
                            height = random.randint(1,2)  
                            inner_flag1 = 1

                        for x2 in range(1,math.floor(maxX) - math.floor(minX)+1):
                            for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                for z2 in range(math.ceil(maxZ) - math.floor(minZ)):

                                    if (x2 == 0) or (y2 == 0) or (z2 == 0):

                                        if (locationMatrix[math.floor(linkToJoinPointX[0] - x2), math.floor(MidPointY - width/2 + y2), math.floor(MidPointZ - height/2 + z2)] == 1):           
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break
                                        else:
                                            flag2 = 0
                                            tempLocationMatrix[math.floor(linkToJoinPointX[0] - x2), math.floor(MidPointY - width/2 + y2), math.floor(MidPointZ - height/2 + z2)] = 1


                                    elif (locationMatrix[math.floor(linkToJoinPointX[0] - x2), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] == 1):           
                                        flag2 = 1
                                        tempLocationMatrix = locationMatrix.copy()
                                        inner_flag1 = 1
                                        break

                                    else:
                                        flag2 = 0
                                        tempLocationMatrix[math.floor(linkToJoinPointX[0] - x2), math.ceil(MidPointY - width/2 + y2), math.ceil(MidPointZ - height/2 + z2)] = 1
                                    if inner_flag1 == 1:
                                        inner_flag2 = 1
                                        flag2 = 1
                                        break
                                if inner_flag2 == 1:
                                        break
                                    
                    elif jointPositionAxis == 4:
                        minX = MidPointX - length/2
                        maxX = minX + length
                        maxY = linkToJoinPointY[0]
                        minY = maxY - width
                        minZ = MidPointZ - height/2
                        maxZ = minZ + height

                        if (minX < 0) or (minY < 0) or (minZ < 0):
                            flag2 = 1
                            tempLocationMatrix = locationMatrix.copy()
                            length = random.randint(1,2) 
                            width = random.randint(1,2) 
                            height = random.randint(1,2) 
                            inner_flag1 = 1

                        for x2 in range(math.ceil(maxX) - math.floor(minX)):
                            for y2 in range(1,math.floor(maxY) - math.floor(minY)+1):
                                for z2 in range(math.ceil(maxZ) - math.floor(minZ)):
                                    
                                    if (x2 == 0) or (y2 == 0) or (z2 == 0):

                                        if (locationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(linkToJoinPointY[0] - y2), math.floor(MidPointZ - height/2 + z2)] == 1):
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break

                                        else:
                                            flag2 = 0
                                            tempLocationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(linkToJoinPointY[0] - y2), math.floor(MidPointZ - height/2 + z2)] = 1


                                    elif (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.floor(linkToJoinPointY[0] - y2), math.ceil(MidPointZ - height/2 + z2)] == 1):
                                        flag2 = 1
                                        tempLocationMatrix = locationMatrix.copy()
                                        inner_flag1 = 1
                                        break

                                    else:
                                        flag2 = 0
                                        tempLocationMatrix[math.ceil(MidPointX - length/2 + x2), math.floor(linkToJoinPointY[0] - y2), math.ceil(MidPointZ - height/2 + z2)] = 1
                                    if inner_flag1 == 1:
                                        inner_flag2 = 1
                                        flag2 = 1
                                        break
                                if inner_flag2 == 1:
                                        break

                    else:
                        minX = MidPointX - length/2
                        maxX = minX + length
                        minY = MidPointY - width/2
                        maxY = minY + width
                        maxZ = linkToJoinPointZ[0]
                        minZ = maxZ - height
                        if (minX < 0) or (minY < 0) or (minZ < 0):
                            flag2 = 1
                            tempLocationMatrix = locationMatrix.copy()
                            length = random.randint(1,2) 
                            width = random.randint(1,2) 
                            height = random.randint(1,2) 
                            inner_flag1 = 1
                            
                        for x2 in range(math.ceil(maxX) - math.floor(minX)):
                            for y2 in range(math.ceil(maxY) - math.floor(minY)):
                                for z2 in range(1,math.floor(maxZ) - math.floor(minZ)+1):
                                    
                                    if (x2 == 0) or (y2 == 0) or (z2 == 0):
                                        if (locationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(MidPointY - width/2 + y2), math.floor(linkToJoinPointZ[1] - z2)] == 1):                                            
                                            flag2 = 1
                                            tempLocationMatrix = locationMatrix.copy()
                                            inner_flag1 = 1
                                            break

                                        else:
                                            flag2 = 0
                                            
                                            tempLocationMatrix[math.floor(MidPointX - length/2 + x2), math.floor(MidPointY - width/2 + y2), math.floor(linkToJoinPointZ[1] - z2)] = 1
            

                                    # if (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.ceil(z2 + linkToJoinPointZ[1])] == positionTaken).all():
                                    elif (locationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.floor(linkToJoinPointZ[1] - z2)] == 1):                                            
                                        flag2 = 1
                                        tempLocationMatrix = locationMatrix.copy()
                                        inner_flag1 = 1
                                        break
                                    else:
                                        flag2 = 0
                                    
                                        tempLocationMatrix[math.ceil(MidPointX - length/2 + x2), math.ceil(MidPointY - width/2 + y2), math.floor(linkToJoinPointZ[1] - z2)] = 1
                                    if inner_flag1 == 1:
                                        inner_flag2 = 1
                                        flag2 = 1
                                        break
                                if inner_flag2 == 1:
                                        break


            locationMatrix = tempLocationMatrix.copy()
            i = 0
            for l in linksAdded:
                if ("Link" + str(i) in linksAdded):
                    i = i+1
                    pass
                else:
                    break
            locationMatrix = tempLocationMatrix.copy()
            linkLenInfo["Link" + str(i)] = [length, width, height,[minX,maxX],[minY,maxY],[minZ,maxZ]]
            linksAdded.append("Link" + str(i))
            connections.append([jointPositionAxis,linkToJoin])  
            grandConnections[linkToJoin+"_"+"Link"+ str(i)] = jointPositionAxis
            self.connections = connections
            randSensorsList.append(random.randint(0,1))

     

            


        self.linkLenInfo = linkLenInfo
        self.grandConnections = grandConnections
        self.randSensorsList = randSensorsList
        self.linksAdded = linksAdded
        self.locationMatrix = locationMatrix.copy()
        self.connections = connections
       
        numSensorNeurons = randSensorsList.count(1)
        randomRow =  random.randint(0,numSensorNeurons - 1)
       
        numLinks = len(linksAdded)
        randomColumn = random.randint(0,numLinks - 1)
        self.weights[randomRow,randomColumn] =  random.random() * 2 - 1


    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        pass


            