from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)  # Adjusted to pass the robotId instead of "body.urdf"
        self.sensors = {}  # Initialize sensors as an empty dictionary
        self.motors = {}
        self.values = {}
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")
    def Prepare_To_Sense(self):
        # Make sure `linkNamesToIndices` is populated by calling `Prepare_To_Simulate` before this method
        for linkName in pyrosim.linkNamesToIndices:
            # Create a SENSOR instance for each link and store it in self.sensors
            #print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

        # Additional code to setup motors for each joint can be similar in approach
    def Sense(self, t):
        for key in self.sensors:
            # print(self.sensors)
            # print(key)
            self.values[t] = self.sensors[key].Get_Value(t)
           # if t == c.LENGTH:
                #print(self.sensors[key])

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            #print(jointName)
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Save_Values(self):
        for key in self.motors:
            self.motors[key].Save_Values()
        for key in self.sensors:
            self.sensors[key].Save_Values()

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("fitness.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()