# AI Skill Gap Learning Recommender

An AI-powered recommendation system that analyzes a user's resume, identifies skill gaps for a chosen career path, and provides personalized recommendations including learning roadmaps, projects, and certifications.

This project was developed as part of the **Artificial Intelligence Internship Program at DecodeLabs** under the Recommendation Systems milestone.

---

# Overview

Choosing the right career path is challenging and many learners struggle to understand which skills they are missing for their desired role.

The AI Skill Gap Learning Recommender solves this problem by:

* Analyzing uploaded resumes
* Extracting existing skills
* Comparing skills against industry role requirements
* Calculating a Career Readiness Score
* Identifying missing skills
* Generating a personalized learning roadmap
* Recommending projects to build
* Suggesting relevant certifications

Instead of generic recommendations, the system provides actionable guidance tailored to a specific target role.

---

# Problem Statement

Many students and professionals know the role they want to pursue but often lack clarity about:

* Which skills they already possess
* Which skills are missing
* What to learn next
* Which projects to build
* Which certifications are valuable

This project bridges that gap through intelligent recommendation logic and skill matching.

---

# Features

### Resume Upload

Upload a PDF resume directly through the web interface.

### Career Selection

Choose a target role:

* AI Engineer
* Data Scientist
* Machine Learning Engineer
* Backend Developer
* Cybersecurity Analyst

### Skill Extraction

The system scans the uploaded resume and extracts relevant skills.

### Career Readiness Score

Calculates a readiness percentage based on matching skills.

Example:

```text
Career Readiness Score: 75%
```

### Missing Skills Detection

Identifies skills required for the selected role but absent from the resume.

Example:

```text
Missing Skills:
- Docker
- AWS
- LangChain
- MLOps
```

### Learning Roadmap Generation

Provides a personalized roadmap for acquiring missing skills.

### Project Recommendations

Suggests portfolio-worthy projects aligned with the selected role.

### Certification Recommendations

Recommends industry-recognized certifications to strengthen career prospects.

---

# How It Works

## Step 1: Upload Resume

The user uploads a PDF resume.

## Step 2: Skill Extraction

The application extracts text from the PDF using PyMuPDF.

## Step 3: Skill Matching

Extracted skills are compared against predefined role requirements.

## Step 4: Readiness Score Calculation

```python
Readiness Score =
(Matched Skills / Required Skills) × 100
```

## Step 5: Recommendation Generation

The system generates:

* Skill Gap Analysis
* Learning Roadmap
* Recommended Projects
* Certifications

---

# System Architecture

```text
Resume Upload
       │
       ▼
PDF Text Extraction
       │
       ▼
Skill Detection Engine
       │
       ▼
Role Skill Database
       │
       ▼
Recommendation Engine
       │
       ▼
Results Dashboard
```

---

# Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask

## Libraries

* PyMuPDF (Resume Parsing)

---

# Project Structure

```text
Project3/
│
├── app.py
├── recommender.py
├── skills_db.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── uploads/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/AyeshaIjazTabassum/Decodelabs-Internship.git
cd Project3
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the Flask server:

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

Open the URL in your browser.

---

# How to Use

## 1. Upload Resume

Select a PDF resume from your computer.

## 2. Select Target Role

Choose one of the available career paths.

Example:

```text
AI Engineer
```

## 3. Analyze Resume

Click:

```text
Analyze Resume
```

## 4. View Recommendations

The system displays:

* Career Readiness Score
* Current Skills
* Missing Skills
* Learning Roadmap
* Recommended Projects
* Certifications

---

# Example Output

```text
Career Readiness Score: 62%

Current Skills:
✓ Python
✓ Machine Learning
✓ TensorFlow

Missing Skills:
✗ Docker
✗ AWS
✗ LangChain
✗ MLOps

Learning Roadmap:
1. Learn Docker
2. Learn AWS
3. Learn LangChain
4. Learn MLOps

Recommended Projects:
- AI Resume Analyzer
- RAG Chatbot
- Medical Image Classifier

Certifications:
- AWS Cloud Practitioner
- Google ML Engineer
```

---

# AI Concepts Used

This project demonstrates several core Artificial Intelligence concepts:

* Recommendation Systems
* Pattern Matching
* Skill Gap Analysis
* Resume Parsing
* Information Extraction
* Rule-Based Recommendations
* Similarity Matching

---

# Future Enhancements

Potential improvements include:

* LinkedIn Profile Analysis
* GitHub Profile Integration
* NLP-based Skill Extraction
* Semantic Similarity Matching
* Machine Learning Recommendations
* Personalized Course Recommendations
* Interactive Skill Radar Charts
* PDF Report Generation
* User Authentication
* Database Integration
* Job Market Analysis

---

# Learning Outcomes

Through this project, the following concepts were explored:

* Flask Web Development
* Frontend and Backend Integration
* Recommendation Engine Design
* Resume Parsing
* Logic-Based AI Systems
* Skill Matching Algorithms
* Career Recommendation Systems

---

# Acknowledgements

Developed as part of the **Artificial Intelligence Internship** at DecodeLabs.

Project Focus:
**AI Recommendation Logic, Matching user profiles with relevant recommendations using similarity and pattern matching techniques.**

---

# License

This project is intended for educational and learning purposes.
