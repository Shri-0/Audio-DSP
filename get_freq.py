
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
