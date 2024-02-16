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
import sys
s = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(s, solutionID)
simulation.Run()
simulation.Get_Fitness()
