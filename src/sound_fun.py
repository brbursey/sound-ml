import time
import sounddevice as sd
import simpleaudio as sa

import soundfile as sf
from playsound import playsound
from scipy.io import wavfile



duration = 2
fs = 32000


def record(filename):
    print("start recording")

    sample_recording = sd.rec(int(duration*fs), fs, 1, blocking=True)
    # sd.wait()
    print("yo stop")

    sf.write(filename, sample_recording, fs)


def play(filename):
    playsound(filename)

def playwave(filename):
    wav_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wav_obj.play()
    play_obj.wait_done()


def combine_sounds(file1, file2, output_file):
    greetings_frames, greetings_data = wavfile.read(file1)
    salutations_frames, salutations_data = wavfile.read(file2)
    combined_data = greetings_data + salutations_data
    sf.write(output_file, combined_data, fs)


filename = 'greetings.wav'

# playwave("./sound files/audio classifier data/cats_dogs/all_data/cat_1.wav")
playwave(filename)





