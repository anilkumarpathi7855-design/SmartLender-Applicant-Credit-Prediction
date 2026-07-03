# Application Architecture – Smart Lender System

## Overview
The Smart Lender Loan Prediction System follows a **Three-Tier Architecture** to ensure scalability, modularity, and separation of concerns. The system is divided into Presentation Layer, Application Layer, and Data/ML Layer.

---

## 1. Presentation Layer (Frontend)
- Built using HTML, CSS, and Bootstrap.
- Provides user interface for loan application input.
- Collects user details such as income, credit history, loan amount, etc.
- Displays prediction results (Approved / Rejected).

---

## 2. Application Layer (Backend)
- Developed using Flask (Python web framework).
- Handles user requests and routes.
- Processes input data received from frontend.
- Communicates with ML model for prediction.
- Returns results back to frontend.

---

## 3. Data / Machine Learning Layer
- Built using Python, Pandas, NumPy, Scikit-learn.
- Performs data preprocessing and feature engineering.
- Trains ML model (Random Forest / XGBoost).
- Saves trained model as `rdf.pkl`.
- Generates predictions based on input data.

---

## Directory Structure
Smart Lender Project is organized as:

- Dataset/
- Training Notebook/
- Flask Application/
- Templates/
- Static Files/
- Model Files

---

## Benefits of This Architecture
- Separation of frontend and backend
- Easy maintenance and debugging
- Scalable for future improvements
- Modular design for ML integration
