from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)  # Adjusted to pass the robotId instead of "body.urdf"
        self.sensors = {}  # Initialize sensors as an empty dictionary
        self.motors = {}
        self.values = {}
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
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
            if t == c.LENGTH:
                print(self.sensors[key])

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            print(jointName)
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for key in self.motors:
            print(self.motors)
            print(key)
            self.motors[key].Set_Value(self.robotId, t)
            # if t == c.LOOP_LENGTH:
            print(self.motors[key])

    def Save_Values(self):
        for key in self.motors:
            self.motors[key].Save_Values()
        for key in self.sensors:
            self.sensors[key].Save_Values()