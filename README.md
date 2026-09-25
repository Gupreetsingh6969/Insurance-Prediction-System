
Insurance Prediction Project

Insurance Prediction using Machine Learning is a data science project that analyzes customer information such as age, gender, BMI, number of children, smoking status, and region to predict medical insurance charges.

The project involves data cleaning, exploratory data analysis (EDA), visualization, feature selection, and machine learning model development. A regression algorithm such as Linear Regression is trained on historical insurance data to learn the relationship between customer attributes and insurance costs. The trained model can then predict the expected insurance charges for new customers.

Key Technologies: Python, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook

Main Steps:

Data collection and preprocessing
Handling missing/duplicate data
Exploratory Data Analysis (EDA)
Data visualization
Encoding categorical variables
Splitting data into training and testing sets
Training a Machine Learning model
Evaluating model performance using MAE, MSE and R²
Predicting insurance charges for new customers

Project Objective:
To use customer and demographic information to build a machine learning model that can estimate medical insurance costs accurately and help understand the factors that influence insurance charges.

App.py
Python
Insurenceproject (2)(1).ipynb
File
linear_regression_model(1).pkl
File
scaler(1).pkl
File
create a readme file for github

Done — I created a GitHub-ready README.md for your Insurance Prediction project based on your uploaded App.py and project notebook.

It includes:

Project overview
Objective
Technologies
Linear Regression model
8 input features
Streamlit application details
Project structure
Installation & run commands
ML workflow
Future improvements
Developer section

Download: 
README.md 

README.md
Document

Library
/
README.md
🏥 Medical Insurance Charges Prediction

A Machine Learning project that predicts medical insurance charges from customer-related information. The project includes data analysis and a Streamlit web application where users can enter customer details and receive an estimated insurance charge.

📌 Project Overview

The Medical Insurance Charges Prediction system uses a trained Linear Regression model to estimate insurance costs based on features such as:

Age
Gender
BMI
Number of children
Smoking status
Region
BMI category

The trained model and scaler are loaded into a Streamlit application for making predictions.

🎯 Objective

The main objective of this project is to:

Analyze medical insurance data.
Understand factors that affect insurance charges.
Preprocess input data for Machine Learning.
Train a regression model.
Predict estimated medical insurance charges for new customer information.
Provide a simple and interactive web interface for predictions.
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib / Seaborn
Jupyter Notebook
Streamlit
Joblib
Linear Regression
🤖 Machine Learning Model

Algorithm: Linear Regression

The Streamlit application loads the trained model and scaler using Joblib. The application transforms the entered customer data and passes it to the model to generate the predicted insurance charge.

📊 Input Features

The prediction application uses 8 model features:

Feature	Description
age	Customer age
is_female	Encoded gender value
bmi	Body Mass Index
children	Number of children
is_smoker	Encoded smoking status
region_southeast	Southeast region indicator
bmi_category_obese	BMI ≥ 30 indicator
region_northwest	Northwest region indicator

The application accepts user-friendly values such as Male/Female, Yes/No, and region names, then converts them into the numerical format required by the model.

🌐 Streamlit Application

The web application provides:

Interactive customer input form
Age slider
Gender selection
BMI input
Children selection
Smoker selection
Region selection
Input summary
Insurance charge prediction
Styled prediction result

The application is configured with the page title Insurance Prediction System and uses a wide Streamlit layout.

📂 Project Structure
Insurance-Project/
│
├── App.py
├── Insurenceproject (2)(1).ipynb
├── linear_regression_model.pkl
├── scaler.pkl
└── README.md

Keep the model and scaler filenames consistent with the filenames used in App.py.

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/insurance-prediction.git
cd insurance-prediction

Install the required libraries:

pip install pandas numpy scikit-learn streamlit joblib matplotlib seaborn
▶️ Run the Project

Start the Streamlit application:

streamlit run App.py

After running the command, Streamlit will provide a local URL in the terminal. Open that URL in your browser.

🔄 How It Works
Customer Input
      ↓
Data Encoding
      ↓
Feature Preparation
      ↓
Scaling
      ↓
Linear Regression Model
      ↓
Predicted Insurance Charges
💡 Example Workflow
Enter the customer's age.
Select gender.
Enter BMI.
Select the number of children.
Select smoking status.
Select the customer's region.
Click Predict Insurance Charges.
The application displays the estimated insurance charge.
👨‍💻 Developer

Gurpreet Singh
BCA Graduate

⚠️ Disclaimer

This project is developed for educational and demonstration purposes. The predicted insurance charge is a machine-learning estimate and should not be treated as an actual insurance quotation or financial/medical advice.

⭐ Future Improvements
Compare multiple regression algorithms.
Add model performance metrics to the web application.
Add prediction history.
Improve validation and error handling.
Deploy the Streamlit application online.
Add more visual analytics and interactive charts.
