import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # Go up one level to get to project root
data_path = os.path.join(parent_dir, "data", "sample_data.csv")

# Load the data
data = pd.read_csv(data_path)

# Title of the visualization page
st.title("Data Visualization")

# Display the data
st.subheader("Sample Data")
st.write(data)

# Create a simple plot
# Create a more meaningful plot
st.subheader("Age by Diabetes Status")
fig, ax = plt.subplots(figsize=(10, 5))
colors = ["blue", "red"]
for i, status in enumerate([0, 1]):
    group = data[data["diabetes"] == status]
    ax.scatter(group["id"], group["age"], label=f"Diabetes: {status}", color=colors[i])
plt.title("Age Distribution by Diabetes Status")
plt.xlabel("ID")
plt.ylabel("Age")
plt.legend()
st.pyplot(fig)
