import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="BoX", pos = [-3,3, 0.5], size = [1, 1, 1])

def Create_Robot():
    pyrosim.Start_URDF("robot.urdf")

    # Torso Cube
    pyrosim.Send_Cube(name="Backleg", pos=[0, 0, 0.5], size=[1, 1, 1])

    # Joint connecting Torso to Leg
    # Adjust the position based on where you want the joint to be exactly.
    pyrosim.Send_Joint(name="Joint1", parent="Backleg", child="Torso", type="revolute", position=[0.5, 0, 1.0])

    # Leg Cube
    pyrosim.Send_Cube(name="Torso", pos=[0.5, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Joint2", parent="Torso", child="Frontleg", type="revolute", position=[1, 0, 0])
    pyrosim.Send_Cube(name="Frontleg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.End()

Create_Robot()

