import os
from flask import Flask
from flask import request
import cat_dog_model as cdm
import sound_features as sf
import numpy as np


app = Flask(__name__)

model = cdm.CatDogModel()


def get_file(filename):
    return f"./sound_files/audio_classifier_data/cats_dogs/all_data/{filename}"


@app.route("/")
def hello():
    create_model()
    return "Hello World!"


@app.route("/predict_existing_sound", methods=['POST'])
def predict():
    print("attempting prediction...")
    prediction = 0.0
    try:
        args = request.args
        if "fileName" in args:
            filename = args['fileName']
        file = get_file(filename)
        features = sf.get_features(file)
        features = np.array([features])
        prediction = model.predict_sound(features)
        prediction = prediction[0][0]
    except Exception as e:
        print("There was an error extacting the features of the sound file: " + str(e))

    if prediction == 0.0:
        return "Error with predicting sound."
    elif prediction >= 0.5:
        return "Cat"
    elif prediction < 0.5:
        return "Dog"
    else:
        return "Unable to tell what the heck that creature is"

def create_model():
    print("Checking to see if model exists...")
    if not os.path.exists("./sound_model.h5"):
        print("Training model...")
        model.create_model()
    print("Model exists. Ready to go!")
    # app.run(host='localhost', port=5000, debug=True)



