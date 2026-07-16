# Sentiment Analysis Web Application

## Project Overview
This project is an end-to-end AI application that predicts the sentiment of user reviews. 
The application uses Machine Learning and Natural Language Processing (NLP) techniques to classify text into Positive and Negative sentiments.

---

# Machine Learning Workflow

## Phase 1: Environment Setup
- Installed required Python libraries.
- Created project structure.
- Downloaded IMDB sentiment dataset.
- Prepared development environment.

Technologies:
- Python
- Google Colab
- Scikit-learn
- Pandas
- NLTK

---

## Phase 2: Dataset Exploration
- Loaded IMDB Dataset using Pandas.
- Analyzed dataset structure.
- Checked reviews and sentiment labels.
- Explored data distribution.

Dataset:
- 50,000 movie reviews
- Two classes:
  - Positive
  - Negative

---

## Phase 3: Data Cleaning
Performed text cleaning:
- Converted text into lowercase.
- Removed unnecessary characters.
- Removed extra spaces.
- Prepared clean text data.

---

## Phase 4: Text Preprocessing
Applied NLP preprocessing techniques:
- Tokenization
- Stopword removal
- Text normalization

---

## Phase 5: Feature Engineering
Converted text into numerical form using:

- TF-IDF Vectorization

TF-IDF helped the machine learning model understand important words from reviews.

---

## Phase 6: Model Training

Machine Learning Algorithm:

- Logistic Regression

Training Process:
- Split dataset into training and testing data.
- Trained classification model.
- Learned patterns from reviews.

---

## Phase 7: Model Evaluation

Evaluated model performance using:

- Accuracy

Model Result:

Accuracy: 88.89%

---

## Phase 8: Model Saving

Saved trained model files:

- model.pkl
- vectorizer.pkl

These files are used later for prediction.

---

# Backend Development

## Phase 9: FastAPI Backend

Developed REST API using FastAPI.

Backend Features:
- Loaded trained ML model.
- Received user text through API.
- Generated sentiment prediction.
- Returned JSON response.

API Endpoint:

POST /predict

Example Response:

{
"text": "I love this movie",
"prediction": "positive"
}

---

# Frontend Development

## Phase 10: User Interface

Created web interface using:

- HTML
- CSS
- JavaScript

Features:
- Text input box
- Predict button
- Sentiment result display

---

## Phase 11: Frontend Backend Integration

Connected frontend with FastAPI using:

- Fetch API
- JSON requests

Workflow:

User Input → Frontend → FastAPI → ML Model → Prediction → Display Result

---

# Final Project Structure

Sentiment-Analysis-WebApp/

backend/
- main.py
- model.pkl
- vectorizer.pkl

frontend/
- index.html
- style.css
- script.js

README.md