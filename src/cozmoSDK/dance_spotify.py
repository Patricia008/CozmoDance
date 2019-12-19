import json
import time

import cozmo

# from CozmoDance.src.pycozmo import dance_moves
from CozmoDance.src.cozmoSDK import dance_moves
from CozmoDance.src.spotify import player


def cozmo_program(robot: cozmo.robot.Robot):
    dm = dance_moves.DanceMoves(robot)
    dm.init_robot()
    sp = player.SpotifyPlayer()

    lp = player.LocalPlayer()

    with open('../../audio_analysis/billie_out.json') as json_file:
        data = json.load(json_file)
        data_beats = data['beats']

        startTime = time.time() * 1000
        lp.start_player()

        time.sleep(data_beats[0]['start'] * 0.5)
        print(f"slept {data_beats[0]['start']}")
        for i in range(16):
            bar = data_beats[4 * i]['duration'] + data_beats[4 * i + 1]['duration'] + data_beats[4 * i + 2][
                'duration'] + data_beats[4 * i + 3]['duration']
            dm.head_down_up_1_bar(2.7, bar=bar) if (i % 4) % 2 == 0 else dm.head_down_up_2_bar(2.7, bar=bar)
            print(
                f'sleeping for = {bar}; current time = {time.time() * 1000}; progress_app = {time.time() * 1000 - startTime};')

        lp.stop_player()


cozmo.setup_basic_logging(general_log_level='DEBUG', protocol_log_level='DEBUG', protocol_log_messages='DEBUG')
cozmo.run_program(cozmo_program)
