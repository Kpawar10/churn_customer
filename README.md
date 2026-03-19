# 📊 Customer Churn Prediction System

An end-to-end Machine Learning project to predict customer churn risk using classification models and deploy it as an interactive web application.

---

## 🚀 Live Demo
👉 [Click here to use the app]([https://churncstmr.streamlit.app/])

---

## 📌 Problem Statement
Customer churn is a major issue for telecom companies.  
This project predicts whether a customer is likely to churn based on their usage patterns and subscription details.

---

## 🧠 Features

- Predicts churn risk (High / Low)
- Displays churn probability score
- Adjustable threshold for business decision-making
- Interactive UI using Streamlit
- Real-time predictions

---

## 📊 Dataset

- 7000+ customer records
- Features include:
  - Tenure
  - Monthly Charges
  - Contract Type
  - Payment Method
  - Internet Service
  - Paperless Billing

---

## 🔍 Exploratory Data Analysis

Key insights:
- Customers with **month-to-month contracts** have higher churn
- **Low tenure** customers are more likely to churn
- **High monthly charges** increase churn probability
- **Electronic check users** show higher churn behavior

---

## ⚙️ Model Building

- Algorithm: Logistic Regression / Classification Model
- Handled class imbalance
- Feature encoding using one-hot encoding
- Evaluated using:
  - Precision
  - Recall
  - F1-score

---

## 🎯 Model Performance

| Metric | Value |
|--------|------|
| Accuracy | ~79% |
| Recall (Churn) | ~81% |
| Precision (Churn) | ~48% |

---

## 🖥️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

