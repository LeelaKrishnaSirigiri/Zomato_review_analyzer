# =============================================================
# FASTAPI BACKEND — WORD2VEC VERSION
# =============================================================

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import joblib
from nltk.corpus import stopwords
import nltk
import re
import numpy as np

# =============================================================
# DOWNLOAD NLTK
# =============================================================
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

# =============================================================
# LOAD MODELS
# =============================================================
svm_model = joblib.load("models/model .pkl")
le = joblib.load("models/label_encoder .pkl")
w2v_model = joblib.load("models/word2vec.pkl")   # ✅ YOUR MODEL

# =============================================================
# TEXT CLEANING
# =============================================================
def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = text.split()
    tokens = [w for w in tokens if w not in stop_words and len(w) > 2]

    return " ".join(tokens)

# =============================================================
# WORD2VEC VECTOR FUNCTION
# =============================================================
def review_to_vector(review, model, vector_size=100):
    words = review.split()

    word_vectors = [
        model.wv[word] for word in words if word in model.wv
    ]

    if len(word_vectors) == 0:
        return np.zeros(vector_size)

    return np.mean(word_vectors, axis=0)

# =============================================================
# FASTAPI APP
# =============================================================
app = FastAPI(
    title="Zomato Sentiment API",
    description="Sentiment Analysis using Word2Vec + Linear SVM",
    version="3.0.0"
)

# =============================================================
# REQUEST MODEL
# =============================================================
class ReviewRequest(BaseModel):
    review: str = Field(..., description="Enter a review (min 3 characters)")

    @field_validator("review")
    def validate_review(cls, v):
        v = v.strip()

        if len(v) < 3:
            raise ValueError("Review must be at least 3 characters")

        if not any(c.isalpha() for c in v):
            raise ValueError("Review must contain letters")

        return v

# =============================================================
# RESPONSE MODEL
# =============================================================
class SentimentResponse(BaseModel):
    review: str
    sentiment: str
    status: str

# =============================================================
# ROUTES
# =============================================================
@app.get("/")
def home():
    return {
        "message": "Zomato Sentiment API (Word2Vec) is running! 🚀",
        "status": "healthy"
    }

@app.post("/predict", response_model=SentimentResponse)
def predict(request: ReviewRequest):

    # Clean text
    cleaned = clean_text(request.review)

    # Convert to Word2Vec vector
    vector = review_to_vector(cleaned, w2v_model).reshape(1, -1)

    # Predict
    pred = svm_model.predict(vector)[0]
    sentiment = le.inverse_transform([pred])[0]

    return SentimentResponse(
        review=request.review,
        sentiment=sentiment,
        status="success"
    )