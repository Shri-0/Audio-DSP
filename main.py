
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt








#frequency - number of times a sine wave repeats in a second. We will use 1k
frequency = 1000

#sampling rate - let's take 48
num_samples = 48000

# sine wave formula : y(t) = A * sin(2 * pi * f * t)

# y(t) is the axis we want to sample to calculate x axis sample t
# A is amplitude
# pi is pi
# f is frequency
# t is our sample

#sampling rate
sampling_rate = 48000.0
amplitude = 16000

file = "test.wav"


#function
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate)
             for x in range(num_samples)]
