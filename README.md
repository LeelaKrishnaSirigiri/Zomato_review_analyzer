# Zomato Sentiment Analysis System

## Problem Statement

Online platforms like Zomato receive a large number of customer reviews every day. Manually analyzing these reviews to understand customer satisfaction is time-consuming and inefficient.

The objective of this project is to build a system that can automatically analyze reviews and classify them as Positive or Negative, helping businesses quickly understand customer feedback.

---

## Overview

This project is an end-to-end machine learning application that performs sentiment analysis on restaurant reviews. It uses Natural Language Processing techniques to convert text into numerical form and applies a trained model to predict sentiment in real time.

---

## System Architecture

```
User (Streamlit UI)
        │
        ▼
FastAPI Backend (/predict)
        │
        ▼
Text Preprocessing
        │
        ▼
Word2Vec (Vector Representation)
        │
        ▼
SVM Model (Prediction)
        │
        ▼
Response to UI
```

---

## Workflow Explanation

1. User enters a review in the interface
2. Input is validated (minimum length and meaningful text)
3. Text is cleaned (lowercase, remove symbols, stopwords)
4. Words are converted into vectors using Word2Vec
5. Vectors are passed to the SVM model
6. Model predicts sentiment (Positive/Negative)
7. Result is displayed to the user

---

## Model Training and Selection

* Multiple models were tested:

  * Logistic Regression
  * Linear SVM
  * SGD Classifier
  * Random Forest

* Evaluation method:

  * 5-Fold Stratified Cross Validation
  * Metrics: Accuracy and F1 Score

* Final model selection:

  * Linear SVM was chosen because it provided stable performance and worked well with text data while maintaining good speed.

---

## Tech Stack

* Frontend: Streamlit
* Backend: FastAPI
* Machine Learning Model: Linear SVM
* NLP Technique: Word2Vec
* Libraries: Scikit-learn, Gensim, NLTK

---

## Project Structure

```
project/
│
├── models/
│   ├── best_svm.pkl
│   ├── word2vec.pkl
│   ├── label_encoder.pkl
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── notebooks/
│   └── training.ipynb
│
└── README.md
```

---

## How to Run

### Start Backend

```
uvicorn main:app --reload
```

### Start Frontend

```
streamlit run app.py
```

---

## Example

Input:

```
The food was excellent and service was fast
```

Output:

```
Positive
```

---

## Conclusion

This project shows how we can use machine learning to automatically classify customer reviews as positive or negative. It combines text processing, a Word2Vec model, and an SVM classifier to give quick and reliable predictions. It also demonstrates how to connect a trained model with a backend and frontend for real-time use.

---

