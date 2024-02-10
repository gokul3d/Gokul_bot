"""import pyrosim.pyrosim as pyrosim



def Create_Robot():
    pyrosim.Start_URDF("robot.urdf")

    # Torso Cube
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.5], size=[1, 1, 1])

    # Joint connecting Torso to Leg
    # Adjust the position based on where you want the joint to be exactly.
    pyrosim.Send_Joint(name="Torso_Leg", parent="Torso", child="Leg", type="revolute", position=[0.5, 0, 1.0])

    # Leg Cube
    pyrosim.Send_Cube(name="Leg", pos=[1.0, 0, 1.5], size=[1, 1, 1])

    pyrosim.End()

Create_Robot()"""

import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    length = 1
    width = 1
    height = 1
    x = -3
    y = 3
    z = 0.5
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    length = 1
    width = 1
    height = 1
    x = 0
    y = 0
    z = 0.5
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z+1], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                       type="revolute", position=".5 0 1")
    pyrosim.Send_Cube(name="BackLeg", pos=[x + .5, y, z-1], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                       type="revolute", position="-.5 0 1")
    pyrosim.Send_Cube(name="FrontLeg", pos=[x + -.5, y, z-1], size=[length, width, height])

    pyrosim.End()


Create_World()
Create_Robot()

