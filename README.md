ML Salary Estimation System

An end-to-end Machine Learning web application that estimates salaries for data science and AI-related job roles using multiple job-related features.

Built using:

Python
Pandas & NumPy
Scikit-learn
Streamlit
Random Forest Regression

🚀 Live Demo

https://ml-salary-estimator.streamlit.app/

📌 Project Overview

This project predicts approximate salaries based on factors such as:

Experience level
Employment type
Remote work ratio
Company size
Job category

The application performs:

Data preprocessing
Feature engineering
Encoding categorical variables
Model training
Salary estimation through a web interface

📊 Dataset Information

Dataset contains:

245 rows
11 columns

Features include:

Work year
Experience level
Employment type
Job title
Salary in USD
Remote ratio
Company location
Company size

🧠 Machine Learning Workflow

1. Exploratory Data Analysis (EDA)

Performed:

Histograms
Boxplots
Distribution analysis
Outlier detection
Skewness analysis

2. Data Preprocessing
   
Removed unnecessary columns
Handled categorical variables
Applied One-Hot Encoding
Grouped job titles into broader categories
Log transformation applied to salary values

3. Feature Engineering

Created meaningful features from:

Job categories
Experience levels
Employment types
Company sizes

4. Models Used

Implemented and compared:

Linear Regression
Decision Tree Regressor
Random Forest Regressor

Final deployed model:

Random Forest Regressor

📈 Evaluation Metrics

Used:

MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)

The project also compares model performance against a baseline model.

💻 Streamlit Web Application

The deployed application allows users to:

Select job-related inputs
Estimate salary instantly
Visualize salary distribution from dataset

🛠️ Tech Stack
Python
Pandas
NumPy
Matplotlib
Scikit-learn
Streamlit
Joblib

📂 Project Structure
ml-salary-estimator/
│
├── app.py
├── salary_model.pkl
├── model_columns.pkl
├── job_salaries.csv
├── requirements.txt
└── EDA.ipynb

▶️ Run Locally

Clone repository:

git clone https://github.com/neetuyadav23/ml-salary-estimator.git

Install dependencies:

pip install -r requirements.txt

Run Streamlit app:

streamlit run app.py

📌 Future Improvements
Add more real-world salary features
Improve model accuracy with larger datasets
Deploy advanced models like XGBoost
Add interactive dashboards
Integrate SHAP explainability

👩‍💻 Author
Neetu


BTech Computer Science Student
Interested in Machine Learning, AI, and Data Science projects.
