import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy as np
import os  # Import the os module

# Define the directory path
data_directory = 'data'

# Check if the directory exists, and if not, create it
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# add gravity
p.setGravity(0,0,-9.8)

# add environment and objects
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/240)

p.disconnect()
#print(backLegSensorValues)
#print(backLegSensorValues)

np.save('data//backLegSensorValues.npy',backLegSensorValues)
np.save('data//frontLegSensorValues.npy',frontLegSensorValues)