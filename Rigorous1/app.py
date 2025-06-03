import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(page_title="Repayment Eligibility Predictor", layout="centered")

# Load the trained binary classifier model
model = pickle.load(open("model.pkl", "rb"))

st.title("💰 Repayment Eligibility Checker")
st.subheader("Predict whether a person is eligible to repay a loan using alternative data.")
st.markdown("This tool uses a trained machine learning model on synthetic socioeconomic features.")

# 🌟 User Inputs
st.write("### 🔧 Enter Individual Details")
age = st.slider("Age", min_value=18, max_value=70, value=30)
night_light = st.slider("Nightlight Intensity (0.1 to 1.0)", min_value=0.1, max_value=1.0, step=0.01, value=0.7)
education = st.selectbox("Education Level", ["No formal", "Primary", "High School", "Graduate"])
employment = st.selectbox("Employment Type", ["Unemployed", "Casual", "Self-employed", "Salaried"])
region = st.selectbox("Region", ["Rural", "Semi-urban", "Urban"])
gov_subsidy = st.radio("Receiving Govt Subsidy?", ["Yes", "No"])
electricity = st.radio("Access to Electricity?", ["Yes", "No"])

# Convert inputs to model-ready DataFrame
input_data = pd.DataFrame([{
    "age": age,
    "night_light": night_light,
    "gov_subsidy": 1 if gov_subsidy == "Yes" else 0,
    "electricity_access": 1 if electricity == "Yes" else 0,
    "education_level_Graduate": int(education == "Graduate"),
    "education_level_High School": int(education == "High School"),
    "education_level_Primary": int(education == "Primary"),
    "education_level_No formal": int(education == "No formal"),
    "employment_type_Salaried": int(employment == "Salaried"),
    "employment_type_Self-employed": int(employment == "Self-employed"),
    "employment_type_Casual": int(employment == "Casual"),
    "employment_type_Unemployed": int(employment == "Unemployed"),
    "region_Urban": int(region == "Urban"),
    "region_Semi-urban": int(region == "Semi-urban"),
    "region_Rural": int(region == "Rural")
}])

# 🧠 Predict + Explain
if st.button("🔍 Predict Eligibility"):
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]  # Probability of class 1

    if prediction == 1:
        st.success(f"✅ This person is likely to repay the loan. (Confidence: {round(proba * 100, 2)}%)")
    else:
        st.error(f"❌ This person may not be eligible to repay. (Confidence: {round((1 - proba) * 100, 2)}%)")

    # SHAP Explainability
    #st.markdown("### 🔎 Model Explanation (SHAP)")
    #explainer = shap.Explainer(model)
    #shap_values = explainer(input_data)

    # Plot SHAP explanation
    #shap.initjs()
    #st.pyplot(shap.plots.waterfall(shap_values[0], show=False))

