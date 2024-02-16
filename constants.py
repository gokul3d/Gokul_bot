import numpy as np

GRAVITY = -9.8

LENGTH = 1000
#
PI = np.pi
# Leg Forces
AMPLITUDE = PI/4.0
FREQUENCY = 20
PHASE_OFFSET = 0

targetAngles = np.linspace(-np.pi, np.pi, 1000)
# how hard the leg motor should apply force maximum
LEG_MOTOR_MAX_FORCE = 20
# time sleep rate
SLEEP_RATE = 1/240

numberOfGenerations = 10
populationSize = 2