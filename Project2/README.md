# AI-Powered Phishing Website Detection System

## Overview

The **AI-Powered Phishing Website Detection System** is a machine learning-based cybersecurity application designed to identify whether a website URL is **safe** or **phishing**.

This project uses **supervised learning** and advanced **feature engineering** techniques to analyze website URLs and detect suspicious phishing patterns commonly used by cybercriminals.

The system provides a modern web interface where users can paste a website URL and instantly receive a security prediction along with a confidence score.

---

# Features

* AI-powered phishing detection
* Real-time URL analysis
* XGBoost machine learning model
* Modern cybersecurity dashboard UI
* URL feature engineering
* HTML structure analysis
* Confidence score prediction
* Responsive and professional frontend
* Flask-based web application

---

# Technologies Used

## Frontend

* HTML5
* CSS3
* Glassmorphism UI Design

## Backend

* Python
* Flask

## Machine Learning

* XGBoost Classifier
* Scikit-learn

## Data Processing

* Pandas
* NumPy

## Feature Extraction

* BeautifulSoup
* Requests
* Tldextract
* URL Parsing

---

# Project Architecture

```bash
Project2/
│
├── dataset/
│   └── phishing.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── train_model.py
├── feature_extraction.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

# How the System Works

The system follows a complete machine learning pipeline:

1. User enters a website URL
2. URL features are extracted
3. Features are processed and scaled
4. Trained XGBoost model analyzes the data
5. Model predicts:

   * Safe Website
   * Phishing Website
6. Confidence score is displayed

---

# Machine Learning Workflow

## Step 1: Dataset Collection

The model is trained using a phishing website dataset containing:

* Legitimate websites
* Phishing websites

Each row contains engineered URL features and labels.

---

## Step 2: Feature Engineering

The system extracts multiple cybersecurity-related features from URLs.

### Extracted Features

| Feature             | Description                      |
| ------------------- | -------------------------------- |
| URL Length          | Detects unusually long URLs      |
| HTTPS Presence      | Checks for secure protocol       |
| Dot Count           | Detects excessive subdomains     |
| Hyphen Count        | Detects suspicious domains       |
| Digit Count         | Detects random numeric patterns  |
| IP Address Presence | Detects IP-based URLs            |
| Suspicious Keywords | Detects phishing words           |
| Path Length         | Detects abnormal URL paths       |
| Query Length        | Detects suspicious query strings |
| HTML Forms          | Detects login forms              |
| iFrames             | Detects hidden phishing content  |

---

## Step 3: Data Preprocessing

The dataset is:

* Cleaned
* Split into training/testing sets
* Scaled using StandardScaler

---

## Step 4: Model Training

The project uses:

```python
XGBoost Classifier
```

### Why XGBoost?

* High accuracy
* Excellent classification performance
* Handles feature importance well
* Industry-standard algorithm
* Fast and scalable

---

## Step 5: Prediction

The trained model predicts whether a website is:

* Safe
* Phishing

The application also displays a confidence score.

---

# User Interface

The project includes a modern cybersecurity-themed UI with:

* Animated gradient background
* Glassmorphism design
* Responsive layout
* Glowing buttons
* Result cards

---

# Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/AyeshaIjazTabassum/Decodelabs-Internship.git
```

---

## 2. Navigate to Project Folder

```bash
cd Project2
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1: Train the Model

```bash
python train_model.py
```

This generates:

* model.pkl
* scaler.pkl

---

## Step 2: Run Flask Application

```bash
python app.py
```

---

## Step 3: Open Browser

```bash
http://127.0.0.1:5000
```

---

# Dataset Format

The dataset should contain the following columns:

```csv
url_length,https,dots,hyphen,at,digits,suspicious_words,ip_address,subdomains,path_length,query_length,special_chars,iframe,forms,label
```

---

# Label Format

| Label | Meaning          |
| ----- | ---------------- |
| 0     | Safe Website     |
| 1     | Phishing Website |

---

# Example URLs for Testing

## Safe Websites

```text
https://google.com
https://github.com
https://openai.com
```

---

## Phishing URLs

```text
http://paypal-login-security-confirm-account.com
http://google.verify-login-alert.ru
```

---

# Model Performance

| Algorithm | Accuracy |
| --------- | -------- |
| XGBoost   | 99%      |

---

# Future Improvements

The project can be upgraded further with:

## Advanced Features

* Deep learning-based screenshot analysis
* Browser extension integration
* Real-time blacklist checking
* WHOIS analysis
* SSL certificate verification
* NLP-based phishing content analysis
* DNS reputation analysis

---

# Use Cases

* Cybersecurity awareness
* URL security scanning
* Browser protection tools
* Educational AI projects
* Cyber threat detection systems

---

# Learning Outcomes

This project demonstrates:

* Supervised machine learning
* Classification algorithms
* Feature engineering
* Flask web development
* Cybersecurity fundamentals
* AI model deployment
* Frontend/backend integration

---

# Project Highlights

* Real-world cybersecurity application
* End-to-end machine learning pipeline
* Interactive AI-powered interface
* Strong portfolio project
* Industry-relevant classification system

---

# Author

Developed as part of the DecodeLabs Artificial Intelligence Internship.

---

# License

This project is for educational and learning purposes.
