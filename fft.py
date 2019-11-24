import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
from scipy.io import wavfile


def get_fft(wav_file):
    frames, data = wavfile.read(wav_file)
    points = len(data)
    spacing = 1.0 / (2*points)
    x2 = np.linspace(0.0, points*spacing, points)
    y2 = data
    plt.plot(x2, y2)
    plt.show()

    fft_y = fft(y2)
    fft_x = np.linspace(0.0, 1/(2.0*spacing), points//2)
    plt.plot(fft_x, 2.0/points * np.abs(fft_y[0:points//2]))
    plt.grid()
    plt.show()


# get_fft("test.wav")
get_fft("./sound files/salutations.wav")
# get_fft("vinny.wav")