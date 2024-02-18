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

numberOfGenerations = 30
populationSize = 10

numSensorNeurons = 4 #Since only four sensors are in contact

numMotorNeurons = 8 #But all joints are actuating all time so leave it untouched

motorJointRange = 0.5