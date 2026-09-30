import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

import cozmoclad
def _skip(*args, **kwargs):
	return None
cozmoclad.assert_clad_match = _skip
cozmoclad.__build_version__ = "00000.00000.00000"

def cozmo_program(robot: cozmo.robot.Robot):
    n = int(input("Vertices: "))
    for i in range(0,n):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(360/n)).wait_for_completed()


cozmo.run_program(cozmo_program)
