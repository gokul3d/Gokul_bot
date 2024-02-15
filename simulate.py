import pybullet as p
import pybullet_data
import time
import sys
import numpy as np
import random
# Assuming pyrosim, constants, and simulation are modules within your project
import pyrosim.pyrosim as pyrosim
import constants as c
from simulation import SIMULATION

# Check if an argument was provided; if not, set a default value or handle appropriately
if len(sys.argv) > 1:
    s = sys.argv[1]
else:
    print("No argument provided. Using default value.")
    s = "default_value"  # Set a default value for 's' or handle the lack of input as needed

simulation = SIMULATION(s)
simulation.Run()
simulation.Get_Fitness()
