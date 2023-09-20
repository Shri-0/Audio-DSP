
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

frame_rate  = 48000.0
infile = "test.wav"
num_samples = 48000
wav_file = wave.open(infile, 'r')
data = wav_file.readframes(num_samples)
wav_file.close()

data = struct.unpack('{n}h'.format(n=num_samples), data)
data = np.array(data)

#converting data to numpy array

data_fft = np.fft.fft(data)
#print(data_fft)

#we are going to get the frequencies we want
frequencies = np.abs(data_fft)

#data_fft[1] will contain frequency parts of 1Hz
#data_fft[2] will contain frequency part of 2Hz
print("The frequency is {} Hz".format(np.argmax(frequencies)))
