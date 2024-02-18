import numpy as np

GRAVITY = -9.8

LENGTH = 10000
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

numberOfGenerations = 1
populationSize = 1

numSensorNeurons = 9

numMotorNeurons = 8