import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Streamlit UI
st.set_page_config(
    page_title="GraphGenius",
    initial_sidebar_state="expanded",
    layout="centered"
)


def main():
    st.title("GraphGenius - Data Visualization Dashboard")
    st.write("GraphGenius is a data visualization dashboard. Users can upload CSV or Excel files to visualize and explore their data easily!")
    
    # File Uploader Widget
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        if uploaded_file.name.endswith('csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('xlsx'):
            data = pd.read_excel(uploaded_file, engine='openpyxl')
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            return
        
        st.write("Uploaded Data:", data)
        
        

if __name__ == "__main__":
    main()
