from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib


app = FastAPI(title="Sentiment Analysis API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


class Review(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is Running!"}


@app.post("/predict")
def predict(review: Review):
    review_vector = vectorizer.transform([review.text])
    prediction = model.predict(review_vector)[0]

    return {
        "text": review.text,
        "prediction": prediction
    }