from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import fitz

from skills_db import roles
from recommender import generate_recommendation

app = Flask(__name__)

SKILLS = [
"Python",
"Machine Learning",
"Deep Learning",
"TensorFlow",
"PyTorch",
"Pandas",
"NumPy",
"SQL",
"AWS",
"Docker",
"LangChain",
"MLOps"
]

def extract_text(pdf_file):

    doc = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in doc:
        text += page.get_text()

    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    pdf = request.files["resume"]

    role = request.form["role"]

    text = extract_text(pdf)

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    result = generate_recommendation(
        found_skills,
        roles[role]
    )

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)