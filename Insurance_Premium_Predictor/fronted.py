import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict_insurance_premium/"

st.set_page_config(page_title="Insurance Premium Predictor")

st.title("💰 Insurance Premium Prediction")
st.markdown("Predict your insurance premium using ML")

# ---------------------------------------------------
# Sidebar Inputs
# ---------------------------------------------------
st.sidebar.header("User Details")

age = st.sidebar.number_input("Age", min_value=1, max_value=100, value=28)

weight = st.sidebar.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)

height = st.sidebar.number_input("Height (cm)", min_value=120, max_value=220, value=170)

income_lpa = st.sidebar.number_input("Income (LPA)", min_value=0.5, max_value=100.0, value=6.5)

city = st.sidebar.text_input("City", value="Delhi")

occupation = st.sidebar.selectbox(
    "Occupation",
    [
        "private_job",
        "government_job",
        "business_owner",
        "freelancer",
        "student",
        "retired",
        "unemployed"
    ]
)

smoker = st.sidebar.radio("Smoker", ["No", "Yes"])

# ---------------------------------------------------
# Convert smoker to boolean
# ---------------------------------------------------
smoker_bool = True if smoker == "Yes" else False

# ---------------------------------------------------
# Predict Button
# ---------------------------------------------------
if st.button("Predict Premium 🚀"):

    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "city": city,
        "occupation": occupation,
        "smoker": smoker_bool
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)

        if response.status_code == 200:
            result = response.json()
            category = result["predicted_premium"]

            st.success(f"Predicted Insurance Premium Category: **{category}**")

            # Optional explanation
            explanation = {
                "Low": "Low premium – lower risk profile",
                "Average": "Average premium – moderate risk",
                "High": "High premium – higher risk profile"
            }
            st.info(explanation.get(category, ""))

        else:
            st.error(f"API Error {response.status_code}: {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server. Make sure it is running.")
