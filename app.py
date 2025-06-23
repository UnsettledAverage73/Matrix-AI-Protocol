import streamlit as st
import requests

# API configuration
API_URL = "http://localhost:8000"  # Change to your deployed URL if needed

# App Title
st.set_page_config(page_title="Income Prediction App")
st.title("📊 Income Prediction App")

# Health Check
with st.spinner("Checking API status..."):
    try:
        ping_response = requests.get(f"{API_URL}/ping")
        if ping_response.status_code == 200 and ping_response.json().get("status") == "ok":
            st.success("✅ API is Online")
        else:
            st.error("❌ API is Offline or Unreachable")
    except:
        st.error("❌ API is Offline or Unreachable")

st.write("---")

# Input Form
with st.form("income_form"):
    st.subheader("Enter Customer Information:")

    occupation = st.selectbox("Occupation", ["Farmer", "Daily Laborer", "Small Shop Owner", "Teacher"])
    upi_txns_month = st.number_input("UPI Transactions/Month", min_value=0)
    mobile_recharge_freq = st.selectbox("Mobile Recharge Frequency", ["Daily", "Weekly", "Monthly"])
    night_light = st.slider("Night Light Intensity", 0, 100, 50)
    education = st.selectbox("Education", ["Primary", "Secondary", "Graduate", "Post-Graduate"])
    is_urban = st.radio("Urban Area?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    bill_payment_consistency = st.radio("Consistent Bill Payment?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    ecommerce_freq = st.number_input("E-commerce Purchases/Month", min_value=0)
    skill_level = st.selectbox("Skill Level", ["Unskilled", "Semi-Skilled", "Skilled"])
    household_size = st.number_input("Household Size", min_value=1)
    market_density = st.slider("Market Density", 0.0, 1.0, 0.5)
    public_transport_access = st.radio("Access to Public Transport?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    housing_type = st.selectbox("Housing Type", ["Kaccha", "Semi-Pucca", "Pucca"])

    submitted = st.form_submit_button("Predict Income")

if submitted:
    input_data = {
        "features": {
            "occupation": occupation,
            "upi_txns_month": upi_txns_month,
            "mobile_recharge_freq": mobile_recharge_freq,
            "night_light": night_light,
            "education": education,
            "is_urban": is_urban,
            "bill_payment_consistency": bill_payment_consistency,
            "ecommerce_freq": ecommerce_freq,
            "skill_level": skill_level,
            "household_size": household_size,
            "market_density": market_density,
            "public_transport_access": public_transport_access,
            "housing_type": housing_type
        }
    }

    try:
        with st.spinner("Making prediction..."):
            response = requests.post(f"{API_URL}/invocations", json=input_data)
            if response.status_code == 200:
                result = response.json()
                predicted_income = result["predicted_income"]
                st.success(f"🎯 Predicted Monthly Income: ₹{predicted_income:,.2f}")
            else:
                st.error("Prediction failed. Please check your input or try again later.")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
