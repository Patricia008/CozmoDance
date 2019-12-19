import math
import time as Time

import cozmo
import numpy as np
from cozmo.util import degrees, distance_mm, speed_mmps


def dance_for_me(robot: cozmo.robot.Robot):
    robot.say_text('dance for me').wait_for_completed()


