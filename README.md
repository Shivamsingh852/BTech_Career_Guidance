# AI-Based Career Guidance System

An intelligent web platform designed as a B.Tech final year project. This system analyzes a user's academic profile, skills, interests, and personality traits using Machine Learning (Decision Tree/KNN) and Natural Language Processing (NLP) to recommend personalized career paths, required skills, and learning resources.

## 🚀 Features

* **User Module:** Secure registration, login, and comprehensive profile assessment forms.
* **AI Recommendation Engine:** Uses `scikit-learn` to process user feature vectors and predict ideal career paths (e.g., Software Engineer, Data Scientist, Graphic Designer).
* **Course & Resource Module:** Dynamically maps the AI prediction to real-world, in-demand skills, online courses (Coursera, edX), and professional certifications.
* **NLP Chatbot:** An integrated, offline TF-IDF intent-matching chatbot to answer career-related queries 24/7 (with optional OpenAI integration).
* **Feedback & Evaluation Loop:** Allows users to rate predictions, continuously storing feedback to improve the model.
* **Administrator Dashboard:** Interactive data visualizations using `Plotly` and `Pandas` to track model accuracy and user satisfaction.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Backend:** Flask, Flask-SQLAlchemy, Flask-Login
* **Database:** SQLite (Easily swappable to MySQL/PostgreSQL)
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **NLP:** NLTK, Scikit-learn (TF-IDF Vectorizer)
* **Frontend:** HTML, CSS, JavaScript
* **Data Visualization:** Plotly

## ⚙️ Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shivamsingh852/BTech_Career_Guidance.git
   cd BTech_Career_Guidance
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the Machine Learning Model:**
   *Generates the synthetic dataset and exports the `.pkl` model.*
   ```bash
   python train_model.py
   ```

4. **Run the Web Application:**
   ```bash
   python run.py
   ```
   *The server will start on `http://127.0.0.1:5001`.*

## 👨‍💻 Usage Guide

* **Students:** Register for a new account, complete your profile assessment (Academic %, Programming Skill, Communication, etc.), and instantly receive your AI-generated career path alongside recommended courses.
* **Admin:** Register an account with the exact username `admin` to unlock the **Admin Dashboard** in the navigation bar. Here, you can view interactive charts of user feedback.


