import cozmo

import cozmoclad
def _skip(*args, **kwargs):
	return None
cozmoclad.assert_clad_match = _skip
cozmoclad.__build_version__ = "00000.00000.00000"

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()
    robot.say_text("Advanced Robotics").wait_for_completed()

cozmo.run_program(cozmo_program,)
