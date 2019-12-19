import time

import cozmo
from cozmo.robot import MAX_HEAD_ANGLE
from cozmo.util import degrees, distance_mm, speed_mmps


class DanceMoves:
    '''The dance moves of Cozmo.'''

    def __init__(self, robot: cozmo.robot.Robot):
        self.robot = robot

    def to_the_left_to_the_right(self):
        self.to_the_left()
        self.to_the_right()
        self.to_the_right()
        self.to_the_left()
        self.to_the_right()

    def to_the_left_to_the_right(self):
        self.to_the_left()
        self.to_the_right()
        self.to_the_right()
        self.to_the_left()
        self.to_the_right()

    def up_n_down(self):
        self.robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
        self.robot.set_lift_height(1.0, in_parallel=True)
        self.robot.wait_for_all_actions_completed()
        self.robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
        self.robot.set_lift_height(0.0, in_parallel=True)
        self.robot.wait_for_all_actions_completed()
        self.robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
        self.robot.set_lift_height(1.0, in_parallel=True)
        self.robot.wait_for_all_actions_completed()
        self.robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
        self.robot.set_lift_height(0.0, in_parallel=True)
        self.robot.wait_for_all_actions_completed()

    def to_the_left(self):
        self.robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
        self.robot.set_lift_height(0.0, in_parallel=True)
        self.robot.turn_in_place(angle=degrees(90), in_parallel=True)
        self.robot.wait_for_all_actions_completed()

    def to_the_right(self):
        self.robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
        self.robot.set_lift_height(1.0, in_parallel=True)
        self.robot.turn_in_place(angle=degrees(-90), in_parallel=True)
        self.robot.wait_for_all_actions_completed()

    def nod(self):
        self.robot.set_lift_height(0.0, in_parallel=True)
        self.robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
        self.robot.wait_for_all_actions_completed()
        self.robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    def michael_dance(self):
        self.robot.turn_in_place(angle=degrees(90)).wait_for_completed()
        self.robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
        self.robot.set_lift_height(1.0, in_parallel=True)
        self.robot.drive_straight(distance_mm(-60), speed_mmps(40), in_parallel=True, should_play_anim=False)
        self.robot.wait_for_all_actions_completed()

        self.robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
        self.robot.wait_for_all_actions_completed()

    def sing(self):
        self.to_the_right()
        self.robot.say_text("touch it").wait_for_completed()
        self.to_the_left()
        self.robot.say_text("bring it").wait_for_completed()
        self.to_the_right()
        self.robot.say_text("pay it").wait_for_completed()
        self.to_the_left()
        self.robot.say_text("watch it").wait_for_completed()

    def forward_aggressive(self):
        self.robot.turn_in_place(angle=degrees(-90)).wait_for_completed()
        self.robot.set_lift_height(1.0).wait_for_completed()
        self.robot.drive_straight(distance_mm(100), speed_mmps(60), in_parallel=True)
        self.robot.set_lift_height(0.5, in_parallel=True)
        self.robot.wait_for_all_actions_completed()
        self.robot.set_lift_height(1.0, in_parallel=True)
        self.robot.wait_for_all_actions_completed()

    def michael_turn(self):
        self.robot.set_lift_height(1.0, in_parallel=True)
        self.robot.turn_in_place(angle=degrees(180), in_parallel=True)
        self.robot.wait_for_all_actions_completed()
        self.robot.set_lift_height(0.2, in_parallel=True)
        self.robot.wait_for_all_actions_completed()
        self.robot.set_lift_height(1.0, in_parallel=True)
        self.robot.wait_for_all_actions_completed()

    async def happy_turn(self):
        await self.robot.turn_in_place(angle=degrees(20)).wait_for_completed()
        await self.robot.turn_in_place(angle=degrees(-40)).wait_for_completed()
        await self.robot.turn_in_place(angle=degrees(40)).wait_for_completed()
        await self.robot.turn_in_place(angle=degrees(-20)).wait_for_completed()

    def turn_right(self):
        self.robot.turn_in_place(angle=degrees(720)).wait_for_completed()

    def turn_left(self):
        self.robot.turn_in_place(angle=degrees(-720)).wait_for_completed()

    async def right_left(self, duration: int, deg_num: int, height: float):
        req_speed = 5000 if duration == 0 else deg_num / duration
        req_sleep = 0.5 if duration == 0 else duration
        self.robot.set_lift_height(height=height, in_parallel=True, duration=duration),
        self.robot.turn_in_place(angle=degrees(deg_num), in_parallel=True, speed=degrees(req_speed))
        await self.robot.wait_for_all_actions_completed()

    async def left_right(self, duration: int, deg_num: int, height: float):
        req_speed = 5000 if duration == 0 else deg_num / duration
        req_sleep = 0.5 if duration == 0 else duration
        self.robot.set_lift_height(height=height, in_parallel=True, duration=duration)
        self.robot.turn_in_place(angle=degrees(deg_num), in_parallel=True, speed=degrees(req_speed))
        await self.robot.wait_for_all_actions_completed()

    def init_robot(self):
        self.robot.set_head_angle(MAX_HEAD_ANGLE, in_parallel=True)
        self.robot.set_all_backpack_lights(cozmo.lights.blue_light)
        self.robot.set_lift_height(0.75, in_parallel=True)
        self.robot.wait_for_all_actions_completed()

    def head_down_up_1_bar(self, speed: float, bar: float):
        half_beat = bar / 8
        self.robot.move_head(-1 * speed)
        time.sleep(half_beat)
        self.robot.stop_all_motors()
        time.sleep(half_beat * 1.5)
        self.robot.move_head(speed / 2)
        time.sleep(half_beat * 4)
        self.robot.stop_all_motors()
        time.sleep(half_beat * 1.5)

    def head_down_up_2_bar(self, speed: float, bar: float):
        quarter_beat = bar / 16
        self.robot.move_head(-1 * speed * 1.2)
        time.sleep(quarter_beat * 1.5)
        self.robot.stop_all_motors()
        time.sleep(quarter_beat * 2)
        self.robot.move_head(speed * 0.6)
        time.sleep(quarter_beat * 3)
        self.robot.stop_all_motors()
        time.sleep(quarter_beat * 1.5)
        self.robot.move_head(-1 * speed)
        time.sleep(quarter_beat * 1.5)
        self.robot.stop_all_motors()
        time.sleep(quarter_beat * 2)
        self.robot.move_head(speed * 0.5)
        time.sleep(quarter_beat * 3)
        self.robot.stop_all_motors()
        time.sleep(quarter_beat * 1.5)



def stop(self):
    self.robot.stop_all_motors()
