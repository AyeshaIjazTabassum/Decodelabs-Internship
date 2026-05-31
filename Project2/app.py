from flask import Flask, render_template, request
import joblib
import numpy as np

from feature_extraction import extract_features

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

# Load scaler
scaler = joblib.load("scaler.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    error = None
    features_list = None

    if request.method == "POST":

        try:

            url = request.form["url"]

            # Add https automatically
            if not url.startswith("http"):
                url = "https://" + url

            # Extract Features
            features = extract_features(url)

            features_list = features

            # Convert to array
            features = np.array(features).reshape(1, -1)

            # Scale
            features = scaler.transform(features)

            # Predict
            pred = model.predict(features)[0]

            # Confidence
            probs = model.predict_proba(features)[0]

            confidence = round(max(probs) * 100, 2)

            # Label
            if pred == 0:
                prediction = "SAFE WEBSITE"

            else:
                prediction = "PHISHING WEBSITE"

        except Exception as e:

            error = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        error=error,
        features=features_list
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )