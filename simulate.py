import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI) # Start PyBullet in GUI mode
p.setGravity(0, 0, -9.8) # Set gravity (optional but recommended)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) # Optional: Set path for PyBullet to find additional data
# Add a ground plane
groundId = p.loadURDF("plane.urdf")
boxId = p.loadSDF("box.sdf")
for i in range(1000): # Number of simulation steps; adjust as needed
    p.stepSimulation()
    time.sleep(1./240.) # Simulation time step; adjust for real-time simulation or faster processing
p.disconnect()
