import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf
from playsound import playsound

duration = 2
fs = 16000


def record():
    print("start recording")

    sample_recording = sd.rec(int(duration*fs), fs, 1, blocking=True)
    # sd.wait()
    print("yo stop")

    plt.plot(sample_recording)
    plt.title("recorded sound")
    plt.show()

    filename = "output.wav"
    sf.write(filename, sample_recording, fs)

def play():
    playsound('output.wav')

# record()
play()