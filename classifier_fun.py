import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import sklearn
import numpy as np

audio_path = "./sound files/test/greetings.wav"
x, sr = librosa.load(audio_path)
ipd.Audio(audio_path)

# show waveplot
plt.figure(figsize=(10, 5))
librosa.display.waveplot(x, sr)
plt.show()

# show spectrogram
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(10, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis="time", y_axis="hz")
plt.colorbar()
plt.show()

# zero crossing rate
n0 = 9000
n1 = 9100
plt.figure(figsize=(10, 5))
plt.plot(x[n0:n1])
plt.grid()
plt.show()
zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
print(sum(zero_crossings))

# spectral centroid
spectral_centroid = librosa.feature.spectral_centroid(x, sr=sr)[0]
spectral_centroid.shape
frames = range(len(spectral_centroid))
t = librosa.frames_to_time(frames)


def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)


librosa.display.waveplot(x, sr=sr, alpha=0.4)
plt.plot(t, normalize(spectral_centroid), color='r')
plt.show()

# spectral rolloff
spectral_rolloff = librosa.feature.spectral_rolloff(x, sr=sr)[0]
librosa.display.waveplot(x, sr=sr, alpha=0.4)
plt.plot(t, normalize(spectral_rolloff), color='r')
plt.show()

#mel frequency cepstral coefficients
mfccs = librosa.feature.mfcc(x, sr=sr)
print(mfccs.shape)
print(np.mean(mfccs[0]))
librosa.display.specshow(mfccs, sr=sr, x_axis='time')
plt.show()