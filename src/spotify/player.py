# shows audio analysis for the given track

from __future__ import print_function  # (at top of module)

import json
import sys
import time

import spotipy
from pynput.keyboard import Controller


class SpotifyPlayer:
    '''The dance moves of Cozmo.'''

    def __init__(self):
        token = "TOKEN"
        self.sp = spotipy.Spotify(auth=token)

    def start_player(self):
        self.sp.start_playback()

    def get_status(self):
        startTime = time.time()
        playback = self.sp.current_playback()
        print(f'{time.time() - startTime} call to get status')
        return {'timestamp': playback['timestamp'], 'progress_ms': playback['progress_ms']}

    def get_audio_analysis(self):
        if len(sys.argv) > 1:
            tid = sys.argv[1]
        else:
            tid = 'spotify:track:5ChkMS8OtdzJeqyybCc9R5'

        start = time.time()
        analysis = self.sp.audio_analysis(tid)
        delta = time.time() - start
        print(json.dumps(analysis, indent=4))
        print("analysis retrieved in %.2f seconds" % (delta,))


class LocalPlayer:

    def __init__(self) -> None:
        self.keyboard = Controller()

    def start_player(self):
        HIDPostAuxKey(NX_KEYTYPE_PREVIOUS)
        HIDPostAuxKey(NX_KEYTYPE_PLAY)

    def stop_player(self):
        HIDPostAuxKey(NX_KEYTYPE_PLAY)


import Quartz

# NSEvent.h
NSSystemDefined = 14

# hidsystem/ev_keymap.h
NX_KEYTYPE_SOUND_UP = 0
NX_KEYTYPE_SOUND_DOWN = 1
NX_KEYTYPE_PLAY = 16
NX_KEYTYPE_NEXT = 17
NX_KEYTYPE_PREVIOUS = 18
NX_KEYTYPE_FAST = 19
NX_KEYTYPE_REWIND = 20


def HIDPostAuxKey(key):
    def doKey(down):
        ev = Quartz.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
            NSSystemDefined,  # type
            (0, 0),  # location
            0xa00 if down else 0xb00,  # flags
            0,  # timestamp
            0,  # window
            0,  # ctx
            8,  # subtype
            (key << 16) | ((0xa if down else 0xb) << 8),  # data1
            -1  # data2
        )
        cev = ev.CGEvent()
        Quartz.CGEventPost(0, cev)

    doKey(True)
    doKey(False)
