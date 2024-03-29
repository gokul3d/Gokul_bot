from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:

 def __init__(self):
     self.physicsClient = p.connect(p.GUI)
     p.setAdditionalSearchPath(pybullet_data.getDataPath())

     # add gravity
     p.setGravity(0, 0, c.GRAVITY)
     #pyrosim.Prepare_To_Simulate(robotId)
     self.world = WORLD()
     self.robot = ROBOT()

 def Run(self):
       for i in range(c.LENGTH):
         p.stepSimulation()
         self.robot.Sense(i)
         self.robot.Think()
         self.robot.Act(i)
         time.sleep(c.SLEEP_RATE)

 def  __del__(self):
     self.robot.Save_Values()
     p.disconnect()