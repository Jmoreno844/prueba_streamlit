import streamlit as st

def about():
    st.title("About This Application")
    st.write("""
        This application is designed to help users understand and manage diabetes.
        It provides various features including data visualization, analysis, and educational resources.
        
        ### Purpose
        The main goal of this app is to empower users with knowledge about diabetes,
        enabling them to make informed decisions regarding their health.

        ### Creators
        This application was developed by a team of health enthusiasts and data scientists
        who are passionate about improving health outcomes through technology.
    """)

if __name__ == "__main__":
    about()