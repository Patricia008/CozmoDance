import scipy.io.wavfile
import pydub
import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy import interpolate

# song_title = 'diamond_heart'
song_title = 'billie'
stereo = True

mp3 = pydub.AudioSegment.from_mp3('../music/' + song_title + '.mp3')
###
# convert to wav
###
mp3.export('../music/wav/' + song_title + '.wav', format="wav")
rate, audData = scipy.io.wavfile.read('../music/wav/' + song_title + '.wav')

print(rate)
print(audData)

#####
# modify file to have smaller sample rate
#####
duration = audData.shape[0] / rate
SAMPLERATE = 380
time_old = np.linspace(0, duration, audData.shape[0])
time_new = np.linspace(0, duration, int(audData.shape[0] * SAMPLERATE / rate))

interpolator = interpolate.interp1d(time_old, audData.T)
new_audio = interpolator(time_new).T

wavfile.write("../music/wav/out.wav", SAMPLERATE, np.round(new_audio).astype(audData.dtype))
rate, audData = scipy.io.wavfile.read('../music/wav/' + 'out' + '.wav')

print(rate)
#####
# if stereo, take only one channel
#####
if stereo:
    channel1 = audData[:, 0]  # left
    channel2 = audData[:, 1]  # right
else:
    channel1 = audData

#####
# normalize data; remove 0 values and make discrete interval
#####
music = channel1[channel1 != 0]
absolute_music = np.vectorize(abs)

music = absolute_music(music)
print(music.shape)


def normalize(x):
    if x < 200:
        return 1
    elif x < 1000:
        return 2
    elif x < 5000:
        return 3
    elif x < 6000:
        return 4
    elif x < 8000:
        return 5
    elif x < 10000:
        return 6
    elif x < 15000:
        return 7
    else:
        return 8


normalize_music = np.vectorize(normalize)
music = normalize_music(music)

###
# generate time vector
###
time = np.arange(0, music.shape[0], 1) / rate

print(music)

np.savetxt(song_title + '_amp.out', music, delimiter=',')
plt.figure(1)
plt.subplot(211)
plt.plot(time, music, linewidth=0.01, alpha=0.7, color='#ff7f00')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
