import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "data", "sample_data.csv")
data = pd.read_csv(data_path)

# Title of the visualization page
st.title("Data Visualization")

# Display the data
st.subheader("Sample Data")
st.write(data)

# Create a simple plot
st.subheader("Sample Plot")
plt.figure(figsize=(10, 5))
plt.plot(data["Column1"], data["Column2"], marker="o")
plt.title("Column1 vs Column2")
plt.xlabel("Column1")
plt.ylabel("Column2")
st.pyplot(plt)
