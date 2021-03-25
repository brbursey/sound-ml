import sound_fun as sf
import matplotlib.pyplot as plt
from numpy.fft import fft
import numpy as np
from scipy.io import wavfile
from scipy.signal import argrelextrema as arg




frames, data1 = wavfile.read("salutations.wav")
frames, data2 = wavfile.read("vinny.wav")
frames, data3 = wavfile.read("test.wav")
frames, test_data = wavfile.read("5000_fs.wav")

plt.plot(test_data)
plt.show()

fft_salutations = fft(data1)
fft_vinny = fft(data2)
fft_test = fft(data3)
fft_test2 = fft(test_data)
#
# plt.plot(fft_test2)
max_values_salutations = arg(fft_salutations, np.greater, order=2000)
max_values_vinny = arg(fft_vinny, np.greater, order=1000)
max_values_test = arg(fft_test, np.greater, order=2000)

# print(max_values_salutations)


def side_by_side_plot():
    fig, axes = plt.subplots(2)
    # plt.plot(fft_test)
    # axes[0].title("fft peaks - test")
    # plt.scatter(max_values_test[0], fft_test[max_values_test[0]], linewidth=0.3, s=50, c='r')

    axes[0].plot(fft_salutations)
    # axes[1].title("fft peaks - salutations")
    axes[0].scatter(max_values_salutations[0], fft_salutations[max_values_salutations[0]], linewidth=0.3, s=50, c='r')

    axes[1].plot(fft_vinny)
    # # plt.title("fft peaks - vinny")
    axes[1].scatter(max_values_vinny[0], fft_vinny[max_values_vinny[0]], linewidth=0.3, s=50, c='r')

    plt.show()






