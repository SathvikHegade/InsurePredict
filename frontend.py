import streamlit as st
import requests

API_URL = "http://127.0.0.1:8003/predict"

st.title("Health Insurance Premium Prediction")

st.markdown("Enter the details below to predict your health insurance premium:")

age=st.number_input("Age",min_value=1,max_value=119,value=30)
weight=st.number_input("weight in kg",min_value=1.0,value=65.0)
height=st.number_input("height in meters",min_value=0.5,max_value=2.5,value=1.7)
income_lpa=st.number_input("Annual income in lpa",min_value=0.1,value=10.0)
smoker=st.selectbox("Are you a smoker?", options=[True, False])
city=st.selectbox("City",options=["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune","Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"])
occupation=st.selectbox("Occupation",options=['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'])

if st.button("Predict Premium"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Premium Category: {result['predicted_category']}")
        else:
            st.error("Error in prediction. Please try again.")
    except requests.RequestException as e:
        st.error(f"Error connecting to API: {e}")