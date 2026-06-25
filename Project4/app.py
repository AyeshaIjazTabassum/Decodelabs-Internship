from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from utils.waste_info import waste_info

import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


model = load_model("model/waste_classifier.keras")

classes = [
    "cardboard",
    "glass",
    "metal",
    "paper",
    "plastic",
    "trash"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    img = image.load_img(
        filepath,
        target_size=(224,224)
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    predicted_class = classes[np.argmax(prediction)]

    confidence = float(np.max(prediction) * 100)

    details = waste_info[predicted_class]

    return jsonify({
        "class": predicted_class,
        "confidence": round(confidence,2),
        "recyclable": details["recyclable"],
        "bin": details["bin"],
        "impact": details["impact"],
        "image": filepath
    })


if __name__ == "__main__":
    app.run(debug=True)