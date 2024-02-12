import matplotlib.pyplot as plt
import numpy as np

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')  # Corrected to load front leg data

# Plotting with explicit colors
plt.plot(backLegSensorValues, 'r-', linewidth=2, label='Back Leg Sensor Values')  # Red line
plt.plot(frontLegSensorValues, 'b-', linewidth=2, label='Front Leg Sensor Values')  # Blue line

plt.xlabel('Time Step')
plt.ylabel('Sensor Value')
plt.title('Sensor Values Over Time')
plt.legend()
plt.show()
