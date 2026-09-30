import time

import math

import cozmo

import cozmoclad
def _skip(*args, **kwargs):
	return None
cozmoclad.assert_clad_match = _skip
cozmoclad.__build_version__ = "00000.00000.00000"

def cozmo_program(robot: cozmo.robot.Robot):
    r = int(input("Radius: "))
    inner = r - 3
    outer = r + 3
    relative = outer/inner
    # Tell Cozmo to drive the left wheel at 35 mmps (millimeters per second),
    # and the right wheel at appropriate relative mmps (so Cozmo will turn in a circle of given radius)
    robot.drive_wheels(35, relative*35)

    # wait until inner wheel has finished circle (the wheels will move while we wait)
    time.sleep(2*math.pi*inner/3.5)


cozmo.run_program(cozmo_program)
