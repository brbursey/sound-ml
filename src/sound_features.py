import librosa
import numpy as np
import os
import pandas as pd

# file = open("./sound files/test/greetings.wav", 'rb')
file_directory = "./sound_files/audio_classifier_data/cats_dogs/all_data"


def get_features(sound_file):
    file_features = []
    x, sr = librosa.load(sound_file)

    zero_crossings = np.mean(librosa.feature.zero_crossing_rate(x))
    file_features.append(zero_crossings)

    spectral_centroid = np.mean(librosa.feature.spectral_centroid(x))
    file_features.append(spectral_centroid)

    spectral_rolloff = np.mean(librosa.feature.spectral_rolloff(x))
    file_features.append(spectral_rolloff)

    mfcc = librosa.feature.mfcc(x, sr=sr)
    for i in range(0, 20):
        file_features.append(np.mean(mfcc[i]))

    return file_features


def create_dataset(soundfile_directory):
    features = ['Filename', 'Zero-Crossing Rate', 'Spectral Centroid', 'Spectral Rolloff']
    for i in range(0, 20):
        features.append(f"MFCC{i}")
    features.append('Category')
    X = []
    for file in os.listdir(soundfile_directory):
        data = []
        filepath = f"{soundfile_directory}/{file}"
        category = file.split('_')[0]
        data.append(file)
        file_data = get_features(filepath)
        for values in file_data:
            data.append(values)
        data.append(category)
        X.append(data)
    df = pd.DataFrame(X, columns = features)
    df.to_csv("./sound files/audio classifier data/data/cats_dogs.csv")


# create_dataset(file_directory)

# print(get_features(file_directory + "/cat_35.wav"))

