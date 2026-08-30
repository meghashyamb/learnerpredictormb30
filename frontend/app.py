import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL - "http://backend:7860"

# Title of the Streamlit app
st.title("Learner Predictor")

# Section for online prediction
st.subheader("Online Prediction")

# Create a form for user input
with st.form("prediction_form"):
    # Input fields for learner features
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    current_occupation = st.selectbox("Current Occupation", ["Professional", "Unemployed", "Student"])
    first_interaction = st.selectbox("First Interaction", ["Website", "Mobile App"])
    profile_completed = st.selectbox("Profile Completed", ["Low", "Medium", "High"])
    website_visits = st.number_input("Website Visits", min_value=1, value=1)
    time_spent_on_website = st.number_input("Time Spent on Website", min_value=1, value=1)
    page_views_per_visit = st.number_input("Page Views per Visit", min_value=1, value=1)
    last_activity = st.selectbox("Last Activity", ["Email Activity", "Phone Activity", "Website Activity"])
    print_media_type1 = st.selectbox("Print Media Type 1", ["Yes", "No"])
    print_media_type2 = st.selectbox("Print Media Type 2", ["Yes", "No"])
    digital_media = st.selectbox("Digital Media", ["Yes", "No"])
    educational_channels = st.selectbox("Educational Channels", ["Yes", "No"])
    referral = st.selectbox("Referral", ["Yes", "No"])

# Convert Userinput into a dataframe
    input_data = pd.DataFrame({
        "age": [age],
        "current_occupation": [current_occupation],
        "first_interaction": [first_interaction],
        "profile_completed": [profile_completed],
        "website_visits": [website_visits],
        "time_spent_on_website": [time_spent_on_website],
        "page_views_per_visit": [page_views_per_visit],
        "last_activity": [last_activity],
        "print_media_type1": [print_media_type1],
        "print_media_type2": [print_media_type2],
        "digital_media": [digital_media],
        "educational_channels": [educational_channels],
        "referral": [referral]
    })

    # Make prediction when the "Predict" button is clicked
    if st.form_submit_button("Predict"):
        # Send a POST request to the backend for prediction
        response = requests.post(f"{BACKEND_URL}/v1/predict", json=input_data.to_dict(orient="records")[0])
        if response.status_code == 200:
            prediction = response.json()["Predicted status of learner"]
            st.success(f"Prediction: {prediction}")
        else:
            st.error("Unable to connect to prediction API. Please try again.")

    # Section for batch prediction
    st.subheader("Batch Prediction")

    # Upload a CSV file for batch prediction
    uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type=["csv"])

    # Make batch prediction when the "Predict Batch" button is clicked
    if st.button("Predict Batch"):
        if uploaded_file is not None:
          if st.button("Predict Batch", type="Primary"):
            response = requests.post(f"{BACKEND_URL}/v1/predictbatch", files={"file": uploaded_file})
            if response.status_code == 200:
              predictions = response.json()
              st.success("Batch Predictions Completed!")
              st.write(predictions)
            else:
              st.error("Unable to connect to prediction API. Please try again.")
