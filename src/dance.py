import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

import numpy as np
import time as Time
import math

from pygame import mixer

###
# should be the same as in audioProcess.py file
###
SAMPLERATE = 380
song_title = 'billie2'
music=[]

def read_music_data():
    music = np.genfromtxt(song_title + '_amp.out', delimiter=',')
    return music

def to_the_left_to_the_right(robot: cozmo.robot.Robot):
    to_the_left(robot)
    to_the_right(robot)
    to_the_right(robot)
    to_the_left(robot)
    to_the_right(robot)

def up_n_down(robot):
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
    robot.set_lift_height(1.0, in_parallel=True)
    robot.wait_for_all_actions_completed()
    robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
    robot.set_lift_height(0.0, in_parallel=True)
    robot.wait_for_all_actions_completed()
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
    robot.set_lift_height(1.0, in_parallel=True)
    robot.wait_for_all_actions_completed()
    robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
    robot.set_lift_height(0.0, in_parallel=True)
    robot.wait_for_all_actions_completed()

def to_the_left(robot):
    action1 = robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
    action2 = robot.set_lift_height(0.0, in_parallel=True)
    action3 = robot.turn_in_place(angle=degrees(90), in_parallel=True)
    action1.wait_for_completed()
    action2.wait_for_completed()
    action3.wait_for_completed()


def to_the_right(robot):
    action1 = robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
    action2 = robot.set_lift_height(1.0, in_parallel=True)
    action3 = robot.turn_in_place(angle=degrees(-90), in_parallel=True)
    action1.wait_for_completed()
    action2.wait_for_completed()
    action3.wait_for_completed()

def nod(robot):
    action1 = robot.set_lift_height(0.0, in_parallel=True)
    action2 = robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
    action1.wait_for_completed()
    action2.wait_for_completed()
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

def michael_dance(robot):
    robot.turn_in_place(angle=degrees(90)).wait_for_completed()
    action1 = robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
    action2 = robot.set_lift_height(1.0, in_parallel=True)
    action3 = robot.drive_straight(distance_mm(-60), speed_mmps(40), in_parallel=True)
    action1.wait_for_completed()
    action2.wait_for_completed()
    action4 = robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
    # action5 = robot.set_lift_height(0.0, in_parallel=True)
    action3.wait_for_completed()
    action4.wait_for_completed()
    # action5.wait_for_completed()


def sing(robot):
    to_the_right(robot)
    robot.say_text("touch it").wait_for_completed()
    to_the_left(robot)
    robot.say_text("bring it").wait_for_completed()
    to_the_right(robot)
    robot.say_text("pay it").wait_for_completed()
    to_the_left(robot)
    robot.say_text("watch it").wait_for_completed()

def forward_aggresive(robot):
    robot.turn_in_place(angle=degrees(-90)).wait_for_completed()
    robot.set_lift_height(1.0).wait_for_completed()
    action1 = robot.drive_straight(distance_mm(100), speed_mmps(60), in_parallel=True)
    action2 = robot.set_lift_height(0.5, in_parallel=True)
    action2.wait_for_completed()
    action2 = robot.set_lift_height(1.0, in_parallel=True)
    action2.wait_for_completed()
    action1.wait_for_completed()

def michael_turn(robot):
    robot.set_lift_height(1.0, in_parallel=True)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
    robot.turn_in_place(angle=degrees(90), in_parallel=True)
    robot.wait_for_all_actions_completed()
    robot.turn_in_place(angle=degrees(-90), in_parallel=True)
    robot.set_lift_height(0.1, in_parallel=True)
    robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
    robot.wait_for_all_actions_completed()
    robot.turn_in_place(angle=degrees(-90), in_parallel=True)
    robot.set_lift_height(1.0, in_parallel=True)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
    robot.wait_for_all_actions_completed()
    robot.turn_in_place(angle=degrees(90), in_parallel=True)
    robot.set_lift_height(0.1, in_parallel=True)
    robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE, in_parallel=True)
    robot.wait_for_all_actions_completed()
    robot.turn_in_place(angle=degrees(90), in_parallel=True)
    robot.set_lift_height(1.0, in_parallel=True)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
    robot.wait_for_all_actions_completed()

def happy_turn(robot):
    robot.turn_in_place(angle=degrees(20)).wait_for_completed()
    robot.turn_in_place(angle=degrees(-40)).wait_for_completed()
    robot.turn_in_place(angle=degrees(40)).wait_for_completed()
    robot.turn_in_place(angle=degrees(-20)).wait_for_completed()

def turn_right(robot):
    robot.turn_in_place(angle=degrees(720)).wait_for_completed()

def turn_left(robot):
    robot.turn_in_place(angle=degrees(-720)).wait_for_completed()


def repeat_action(robot, action, n):
    for i in range(0, n):
        action(robot)


def dance_to_music(robot, music, startTime, dance_moves):
    time = np.arange(0, music.shape[0], 1) / SAMPLERATE
    nowTime = Time.time() - startTime
    print(nowTime)
    print(music[0])
    print(time.shape)
    # for x in np.nditer(time):
    #     print(x, end=' ')

    lights = [cozmo.lights.blue_light, cozmo.lights.red_light, cozmo.lights.white_light, cozmo.lights.green_light]

    ###
    # Until the song ends
    ###
    light_index = 0
    while nowTime < time[time.shape[0]-1]:
        robot.set_all_backpack_lights(lights[light_index])
        if light_index == 3:
            light_index = 0
        else:
            light_index += 1

        nowTime = Time.time() - startTime
        ###
        # Find the amplitude for current time
        ###
        amp = find_amp_at_current_time(nowTime, time, music)
        if amp == False:
            continue
        # if amp != prevAmp:
        print(int(amp))
        dance_moves[int(amp)](robot)


def find_amp_at_current_time(nowTime, time, music):
    for idx, val in np.ndenumerate(time):
        if math.ceil(val) == math.ceil(nowTime):
            return music[idx]
    return False


def cozmo_program(robot: cozmo.robot.Robot):

    robot.set_robot_volume(1.0)

    music = read_music_data()
    # robot.say_text('start').wait_for_completed()
    robot.set_backpack_lights(cozmo.lights.blue_light, cozmo.lights.white_light, cozmo.lights.green_light,
                              cozmo.lights.red_light, cozmo.lights.blue_light)
    dance_moves = [1]
    dance_moves.insert(1, nod)
    dance_moves.insert(2, nod)
    dance_moves.insert(3, michael_dance)
    dance_moves.insert(4, michael_turn)
    dance_moves.insert(5, up_n_down)
    dance_moves.insert(6, forward_aggresive)
    dance_moves.insert(7, turn_left)
    dance_moves.insert(8, turn_right)
    dance_moves.insert(9, turn_left)

    mixer.init()
    mixer.music.load('../music/' + song_title + '.mp3')
    startTime = Time.time()
    mixer.music.play()
    dance_to_music(robot, music, startTime, dance_moves)
    robot.say_text('meow').wait_for_completed()

cozmo.run_program(cozmo_program)
