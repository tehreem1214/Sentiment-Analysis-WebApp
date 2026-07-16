import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Load dataset
df = pd.read_csv("Sentiment/IMDB Dataset.csv")

# Check columns
print(df.head())

# Split data
X = df["review"]
y = df["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text into numbers
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X_train_vector = vectorizer.fit_transform(X_train)

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X_train_vector, y_train)


# Save model
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")


# Accuracy check
accuracy = model.score(
    vectorizer.transform(X_test),
    y_test
)

print("Accuracy:", accuracy)
print("Model saved successfully!")