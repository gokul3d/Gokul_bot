import pyrosim.pyrosim as pyrosim

# Initial dimensions of each block
length = 1
width = 1
height = 1

# Initial position (x, y, z)
# The first block's bottom surface is at ground level
x = 0
y = 0
z = height / 2  # Starting z-position to place the bottom of the first block at ground level

pyrosim.Start_SDF("boxes.sdf")  # Start creating the SDF file

# Loop to create and position each block
for i in range(10):  # Iterates 10 times to create 10 blocks
    # Send a cube with the current dimensions and position
    pyrosim.Send_Cube(name=f"Box{i}", pos=[x, y, z], size=[length, width, height])

    # Update z position for the next block to stack it directly on top of the current one
    z += height  # Move z up by one block height for the next block

pyrosim.End()  # Finish creating the SDF file
