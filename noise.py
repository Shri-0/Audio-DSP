

import numpy as np
import wave
import struct
import matplotlib.pyplot as plt


#we create a noisy sine wave and clean up the noise

frequency = 1000
noisy_freq = 50
num_samples = 48000

# sampling rate

sampling_rate = 48000.0
nframes = num_samples
comptype = "NONE"
compname = "not compressed"
nchannels = 1
sampwidth = 2
amplitude = 16000


sine_wav = [np.sin(2 * np.pi * frequency * x1/sampling_rate)
            for x1 in range(num_samples)]

sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/sampling_rate)
            for x1 in range(num_samples)]


#convert into num.py arrays

sine_wave = np.array(sine_wav)
noise_wav = np.array(sine_noise)
file = "testing.wav"

#put them together

combined_signal = sine_wave + noise_wav

'''
wav_file = wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(
    sampling_rate), nframes, comptype, compname))
# opening the file and setting the parameters

for s in combined_signal:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
'''


