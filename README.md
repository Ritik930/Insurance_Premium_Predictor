# 🏥 Insurance Premium Prediction System

An end-to-end **Machine Learning application** that predicts an **insurance premium category** (`Low`, `Average`, `High`) based on user demographics and lifestyle factors.

The project uses **FastAPI** for backend ML inference and **Streamlit** for an interactive frontend.

---

## 🚀 Features

- 🧠 Machine Learning–based insurance premium prediction
- ⚡ FastAPI backend for model inference
- 🎨 Streamlit frontend for user interaction
- 📊 Automatic feature engineering (BMI, age group, lifestyle risk, city tier)
- 🔍 Swagger API documentation
- 🧪 Easy to test and extend

---

## 🏗️ Tech Stack

### Backend
- Python
- FastAPI
- Pydantic
- Pandas
- Pickle

### Frontend
- Streamlit
- Requests

### Machine Learning
- Scikit-learn
- Classification model (`Low / Average / High`)

---

## 📁 Project Structure

insurance_prediction/
│
├── insurance/
│ ├── main.py # FastAPI backend
│ ├── model.pkl # Trained ML model
│
├── fronted.py # Streamlit frontend
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ How It Works

1. User enters personal and lifestyle details in the Streamlit UI
2. Streamlit sends a POST request to the FastAPI backend
3. FastAPI performs feature engineering:
   - BMI calculation
   - Age grouping
   - Lifestyle risk
   - City tier mapping
4. The ML model predicts the **insurance premium category**
5. The result is displayed on the frontend

---

## 🧠 Model Inputs

| Feature | Description |
|------|------------|
| Age | User age |
| Weight | Weight in kg |
| Height | Height in cm |
| Income | Annual income (LPA) |
| Smoker | Smoking status |
| City | User city |
| Occupation | Employment type |

### Engineered Features
- BMI
- Age Group
- Lifestyle Risk
- City Tier

---

## 📌 API Endpoint

### Predict Insurance Premium Category

**POST**
/predict_insurance_premium/

bash
Copy code

### Request Body
```json
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
json
Copy code
{
  "predicted_premium": "Average"
}
▶️ How to Run the Project
1️⃣ Create Virtual Environment & Install Dependencies
bash
Copy code
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
2️⃣ Start FastAPI Backend
bash
Copy code
uvicorn insurance.main:app --reload
Open Swagger UI:

arduino
Copy code
http://127.0.0.1:8000/docs
3️⃣ Start Streamlit Frontend
bash
Copy code
streamlit run fronted.py
Open in browser:

arduino
Copy code
http://localhost:8501
🧪 Sample Output
yaml
Copy code
Predicted Insurance Premium Category: High
Explanation:

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

Handling categorical ML outputs

API response standardization

🚀 Future Improvements
Predict exact premium amount

Add probability/confidence scores

User authentication

Database integration

Docker & cloud deployment

👨‍💻 Author
Ritik Kumar
Final-year student | Backend & Machine Learning Enthusiast
