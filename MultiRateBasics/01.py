import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
from IPython.display import Audio, display
import librosa


fs = 44100
f = 400.0

s = np.sin(2*np.pi*f*np.arange(0, 1, 1.0/fs))

ipd.display(ipd.Audio(s, rate=fs))

plt.figure(figsize=(10, 8))
plt.plot(s[0:1000])
plt.grid()
#plt.show()
