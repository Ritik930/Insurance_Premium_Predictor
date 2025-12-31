from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal
import pickle
from fastapi.responses import JSONResponse
import pandas as pd
import os

# ---------------------------------------------------
# Load ML model (SAFE absolute path)
# ---------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ---------------------------------------------------
# FastAPI app
# ---------------------------------------------------
app = FastAPI(title="Insurance Premium Prediction API")

# ---------------------------------------------------
# City tiers
# ---------------------------------------------------
tier_1_cities = [
    "Mumbai", "Delhi", "Bangalore", "Chennai",
    "Kolkata", "Hyderabad", "Pune"
]

tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna",
    "Ranchi", "Visakhapatnam", "Coimbatore", "Bhopal",
    "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur",
    "Raipur", "Amritsar", "Varanasi", "Agra", "Dehradun",
    "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram",
    "Ludhiana", "Nashik", "Allahabad", "Udaipur",
    "Aurangabad", "Hubli", "Belgaum", "Salem",
    "Vijayawada", "Tiruchirappalli", "Bhavnagar",
    "Gwalior", "Dhanbad", "Bareilly", "Aligarh",
    "Gaya", "Kozhikode", "Warangal", "Kolhapur",
    "Bilaspur", "Jalandhar", "Noida", "Guntur",
    "Asansol", "Siliguri"
]

# ---------------------------------------------------
# Request Schema
# ---------------------------------------------------
class UserInput(BaseModel):
    age: int = Field(..., example=28)
    weight: float = Field(..., example=70.5)
    height: int = Field(..., example=170)
    income_lpa: float = Field(..., example=6.5)
    smoker: bool = Field(..., example=False)
    city: str = Field(..., example="Delhi")
    occupation: Literal[
        "retired",
        "freelancer",
        "government_job",
        "student",
        "unemployed",
        "business_owner",
        "private_job"
    ]

    # -------------------------------
    # Computed fields
    # -------------------------------
    @computed_field
    @property
    def bmi(self) -> float:
        height_m = self.height / 100
        return round(self.weight / (height_m ** 2), 2)

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 30:
            return "young"
        elif self.age < 50:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high_risk"
        elif self.smoker and self.bmi > 27:
            return "medium_risk"
        return "low_risk"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3

# ---------------------------------------------------
# Prediction API
# ---------------------------------------------------
@app.post("/predict_insurance_premium/")
async def predict_insurance_premium(data: UserInput):

    input_df = pd.DataFrame([{
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "occupation": data.occupation,
        "income_lpa": data.income_lpa
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200,content={"predicted_premium": prediction})
