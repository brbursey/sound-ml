import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split as tts


class CatDogModel:

    def __init__(self):
        self.model = tf.keras.Sequential()

    def create_model(self):
        data = pd.read_csv("./sound files/audio classifier data/data/cats_dogs.csv")
        label = data.columns[-1]
        data = data.drop(['Unnamed: 0', 'Filename'], axis=1)
        X = self.__scale_data(data)
        y = self.__encode_data(data, label)

        X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2)
        self.train_model(X_train, y_train)

    def train_model(self, X_train, y_train):
        layers = tf.keras.layers
        self.model.add(layers.Dense(10, activation='relu', input_shape=(X_train.shape[1],)))
        self.model.add(layers.Dense(8, activation='relu'))
        self.model.add(layers.Dense(4, activation='relu'))
        self.model.add(layers.Dense(4, activation='hard_sigmoid'))
        self.model.add(layers.Dense(1, activation='hard_sigmoid'))
        self.model.compile(optimizer='rmsprop',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        self.model.fit(X_train, y_train, epochs=30, batch_size=128)

        self.model.save('sound_model.h5')

    def predict_sound(self, data):
        loaded_model = tf.keras.models.load_model('sound_model.h5')
        return loaded_model.predict(data)

    def __encode_data(self, dataframe, label_to_encode):
        y = dataframe[label_to_encode]
        encoder = LabelEncoder()
        y = encoder.fit_transform(y)
        return y

    def __scale_data(self, dataframe):
        scaler = StandardScaler()
        X = scaler.fit_transform(np.array(dataframe.iloc[:, :-1], dtype=float))
        return X





