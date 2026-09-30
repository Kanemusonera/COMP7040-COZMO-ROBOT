import time

import cozmo

import cozmoclad
def _skip(*args, **kwargs):
	return None
cozmoclad.assert_clad_match = _skip
cozmoclad.__build_version__ = "00000.00000.00000"

def cozmo_program(robot: cozmo.robot.Robot):
    # Tell the head motor to start lowering the head (at 5 radians per second)
    robot.move_head(-5)
    # Tell the lift motor to start lowering the lift (at 5 radians per second)
    robot.move_lift(-5)
    # Tell Cozmo to drive the left wheel at 25 mmps (millimeters per second),
    # and the right wheel at 50 mmps (so Cozmo will drive Forwards while also
    # turning to the left
    robot.drive_wheels(25, 50)

    # wait for 3 seconds (the head, lift and wheels will move while we wait)
    for i in range (0,30):
        time.sleep(0.1)
        print("Left wheel speed: "+str(robot.left_wheel_speed.speed_mmps)+" Right wheel speed: "+str(robot.right_wheel_speed.speed_mmps))

    # Tell the head motor to start raising the head (at 5 radians per second)
    robot.move_head(5)
    # Tell the lift motor to start raising the lift (at 5 radians per second)
    robot.move_lift(5)
    # Tell Cozmo to drive the left wheel at 50 mmps (millimeters per second),
    # and the right wheel at -50 mmps (so Cozmo will turn in-place to the right)
    robot.drive_wheels(50, -50)

    # wait for 3 seconds (the head, lift and wheels will move while we wait)
    for i in range (0,30):
        time.sleep(0.1)
        print("Left wheel speed: "+str(robot.left_wheel_speed.speed_mmps)+" Right wheel speed: "+str(robot.right_wheel_speed.speed_mmps))
    


cozmo.run_program(cozmo_program)
