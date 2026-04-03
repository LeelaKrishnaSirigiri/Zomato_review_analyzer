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

This project demonstrates how machine learning and web technologies can be combined to build a practical sentiment analysis system that provides real-time predictions.

---

## Possible Questions and Answers (Viva)

**1. Why did you choose SVM?**
SVM performs well on text classification problems and provides a good balance between accuracy and speed. It also works effectively with high-dimensional data like text vectors.

**2. Why did you use Word2Vec instead of TF-IDF?**
Word2Vec captures semantic meaning of words by representing them as dense vectors, whereas TF-IDF only captures frequency. This helps the model understand context better.

**3. What is Word2Vec?**
Word2Vec is a technique that converts words into numerical vectors such that similar words have similar vector representations.

**4. How did you evaluate your model?**
I used 5-Fold Stratified Cross Validation and evaluated performance using accuracy and F1 score.

**5. What is the role of FastAPI in this project?**
FastAPI is used to create a backend API that handles requests, processes input, and returns predictions.

**6. What is the role of Streamlit?**
Streamlit is used to build the user interface where users can input reviews and view predictions.

**7. What preprocessing steps did you apply?**
Lowercasing, removing special characters, removing stopwords, and cleaning extra spaces.

**8. Can this project be improved?**
Yes, it can be improved by using deep learning models like LSTM or BERT and by adding a neutral sentiment class.
