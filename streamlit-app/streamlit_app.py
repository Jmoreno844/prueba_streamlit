import streamlit as st
import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "data", "sample_data.csv")
data = pd.read_csv(data_path)

# Set the title of the app
st.title("Diabetes Prediction App")


# Display the data
st.write("Sample Data", data)

# Create a sidebar for user input
st.sidebar.header("User Input")

# Example input fields
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=25)
bmi = st.sidebar.number_input("BMI", min_value=0.0, max_value=50.0, value=22.0)
glucose = st.sidebar.number_input(
    "Glucose Level", min_value=0, max_value=300, value=100
)

# Button to make prediction
if st.sidebar.button("Predict"):
    # Placeholder for prediction logic
    st.write("Prediction logic goes here.")

# About section
if st.sidebar.checkbox("About"):
    st.subheader("About this App")
    st.write("This app predicts diabetes based on user input data.")
