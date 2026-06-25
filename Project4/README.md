# Smart Waste Classification & Recycling Advisor

An AI-powered web application that automatically identifies waste materials from images and provides recycling recommendations, disposal guidance and environmental impact insights.

Built using **Flask**, **TensorFlow**, **MobileNetV2**, **HTML**, **CSS** and **JavaScript**, this project demonstrates the practical application of computer vision in environmental sustainability.

---

## Features

### Waste Image Classification

Upload an image of waste material and let the AI model identify its category.

### Recycling Recommendations

Get instant information about whether the item is recyclable or not.

### Disposal Guidance

Receive recommendations on the correct disposal bin for each waste category.

### Environmental Impact Insights

Learn how proper disposal and recycling can positively impact the environment.

### Confidence Score

View the model's confidence level for every prediction.

### Modern User Interface

* Responsive design
* Glassmorphism effects
* Green sustainability theme
* Animated gradients
* Interactive image preview
* Loading animations

---

# Technologies Used

## Backend

* Python
* Flask

## Machine Learning

* TensorFlow
* Keras
* MobileNetV2 (Transfer Learning)

## Frontend

* HTML5
* CSS3
* JavaScript

## Dataset

* TrashNet Dataset

---

# Project Structure

```text
Porject4/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   ├── cardboard/
│   ├── glass/
│   ├── metal/
│   ├── paper/
│   ├── plastic/
│   └── trash/
│
├── model/
│   └── waste_classifier.keras
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── uploads/
│
└── templates/
    └── index.html
```

---

# Machine Learning Approach

This project uses **Transfer Learning** with MobileNetV2.

### Why MobileNetV2?

* Lightweight architecture
* Fast training
* Excellent performance on small datasets
* Suitable for deployment on resource-constrained systems

### Training Strategy

1. Load pre-trained MobileNetV2 weights from ImageNet
2. Freeze base layers
3. Train custom classification layers
4. Fine-tune upper MobileNetV2 layers
5. Save the optimized model for inference

### Data Augmentation

The model uses:

* Rotation
* Zoom
* Width Shift
* Height Shift
* Horizontal Flip
* Shear Transformations

to improve generalization and reduce overfitting.

---

# Waste Categories

The model classifies waste into six categories:

| Category  | Description                               |
| --------- | ----------------------------------------- |
| Cardboard | Packaging boxes and cartons               |
| Glass     | Bottles, jars, and glass containers       |
| Metal     | Aluminum cans and metal objects           |
| Paper     | Newspapers, notebooks, and paper products |
| Plastic   | Plastic bottles and containers            |
| Trash     | Non-recyclable waste                      |

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd Project4
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Train the Model

Download the TrashNet dataset and place it inside the `dataset` directory.

Run:

```bash
python train_model.py
```

The trained model will be saved as:

```text
model/waste_classifier.keras
```

---

# Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# How to Use

1. Launch the application.
2. Upload a waste image.
3. Click **Analyze Waste**.
4. View:

   * Predicted waste category
   * Confidence score
   * Recycling status
   * Disposal recommendation
   * Environmental impact information

---

# Environmental Impact

This project promotes responsible waste management by helping users:

* Reduce landfill waste
* Improve recycling habits
* Increase environmental awareness
* Encourage sustainable disposal practices

---

# Future Improvements

Potential enhancements include:

* Real-time webcam waste detection
* Waste detection using object detection models (YOLO)
* Recycling statistics dashboard
* User scan history
* PDF report generation
* Cloud deployment
* Mobile application integration
* Multi-language support

---

# Learning Outcomes

Through this project, the following concepts were explored:

* Computer Vision
* Transfer Learning
* Deep Learning
* Flask Web Development
* Model Deployment
* Frontend Development
* Data Augmentation
* Sustainable AI Applications

---

# Author

**Ayesha Ijaz**

AI Intern at DecodeLabs

---

# License

This project is developed for educational and internship purposes.

```
```
