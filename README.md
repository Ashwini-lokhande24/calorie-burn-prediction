#  Calorie Burn Prediction

A machine learning web application that predicts calories burned during exercise.

## About
Built as part of MCA Data Science curriculum at Sri Balaji University, Pune.

## Tech Stack
Core Programming Language used - Python, Pandas, NumPy
For Model Building - Scikit-learn (SVR, Random Forest, Decision Tree, Linear Regression)
Web Application - Flask, HTML, CSS
Development Environment - Jupyter Notebook

## Models Trained
| Model             | R² Score |
|-------------------|----------|
| Linear Regression | 0.9845   |
| Decision Tree     | 0.9920   |
| Random Forest     | 0.9979   |
| SVR               | 0.9999   |

## How to Run
1. Install dependencies: `pip install flask scikit-learn numpy pandas`
2. Run: `python calorie_app/app.py`
3. Open: `http://127.0.0.1:5000`
