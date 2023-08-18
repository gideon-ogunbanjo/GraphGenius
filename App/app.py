import streamlit as st
import pandas as pd

# Streamlit UI
st.set_page_config(
    page_title="GraphGenius",
    initial_sidebar_state="expanded",
    layout="centered"
)


def main():
    st.title("GraphGenius - Data Visualization Dashboard")
    st.write("GraphGenius is a data visualization dashboard. Users can upload CSV or Excel files to visualize and explore their data easily!")
    
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)  # Use pd.read_excel() for Excel files
        st.write("Uploaded Data:", data)

if __name__ == "__main__":
    main()
