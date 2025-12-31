# 🏥 Insurance Premium Prediction System

An end-to-end Machine Learning application that predicts an insurance premium category (Low, Average, High) based on user demographics and lifestyle factors.
The system uses FastAPI for backend inference and Streamlit for an interactive frontend.

🚀 Features

🧠 Machine Learning–based premium category prediction

⚡ FastAPI backend for model inference

🎨 Streamlit frontend for user interaction

📊 Automatic feature engineering (BMI, age group, lifestyle risk, city tier)

🔍 Swagger API documentation

🧪 Easy to test and extend

🏗️ Tech Stack
Backend

Python

FastAPI

Pydantic

Pandas

Pickle (for model loading)

Frontend

Streamlit

Requests

ML

Scikit-learn (trained model)

Classification model (Low / Average / High)

📁 Project Structure
insurance_prediction/
│
├── insurance/
│   ├── main.py          # FastAPI backend
│   ├── model.pkl        # Trained ML model
│
├── fronted.py           # Streamlit frontend
├── requirements.txt
└── README.md

⚙️ How It Works

User enters personal and lifestyle details in the Streamlit UI

Streamlit sends a POST request to FastAPI

FastAPI:

Computes derived features (BMI, risk level, city tier)

Passes data to the ML model

Model predicts insurance premium category

Result is displayed on the UI

🧠 Model Inputs
Feature	Description
Age	User age
Weight	Weight in kg
Height	Height in cm
Income	Annual income (LPA)
Smoker	Smoking status
City	User city
Occupation	Employment type
Engineered Features

BMI

Age Group

Lifestyle Risk

City Tier

📌 API Endpoint
Predict Insurance Premium Category

POST

/predict_insurance_premium/

Request Body
{
  "age": 30,
  "weight": 65,
  "height": 170,
  "income_lpa": 10,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}

Response
{
  "predicted_premium": "Average"
}

▶️ How to Run the Project
1️⃣ Create Virtual Environment & Install Dependencies
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

2️⃣ Start FastAPI Backend
uvicorn insurance.main:app --reload


Open Swagger Docs:

http://127.0.0.1:8000/docs

3️⃣ Start Streamlit Frontend
streamlit run fronted.py


Open:

http://localhost:8501

🧪 Sample Output
Predicted Insurance Premium Category: High


With explanation:

High premium – higher risk profile

🎯 Use Cases

Insurance risk assessment

Customer segmentation

Premium category estimation

ML model deployment practice

🧠 Key Learnings

Feature engineering for ML models

Serving ML models using FastAPI

Frontend–backend integration using Streamlit

Handling real-world data inconsistencies

API response standardization

🚀 Future Improvements

Predict exact premium amount

Add probability scores

User authentication

Database integration

Docker & cloud deployment

👨‍💻 Author

Ritik Kumar
Final-year student | Backend & ML enthusiast
