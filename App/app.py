import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import io
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

st.set_option('deprecation.showPyplotGlobalUse', False)
# Streamlit UI
st.set_page_config(
    page_title="GraphGia",
    layout="centered",
)
st.title("GraphGia - Data Visualization & Exploration Tool")
st.write("GraphGia is a data visualization & Exploration tool. Upload your CSV or Excel files and visualize, explore, clean and manipulate your data easily!")

# File Uploader Widget
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('csv'):
        data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('xlsx'):
        data = pd.read_excel(uploaded_file, engine='openpyxl')
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
    
    st.write("Uploaded Data:", data)
    # # Seaborn Heatmap
    # # Show Heatmap Button
    # if st.button("Show Dataset Heatmap"):
    #     st.subheader("Seaborn Heatmap")
    #     plt.figure(figsize=(10, 6))
        
    #     # Select numeric columns for heatmap
    #     numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    #     selected_columns = st.multiselect("Select Columns for Heatmap", numeric_columns)
        
    #     if selected_columns:
    #         sns.heatmap(data[selected_columns].corr(), annot=True, cmap='coolwarm')
    #         st.pyplot()

    # Additional Information Button
    if st.button("Show Extended Dataset Information"):
        st.subheader("Dataset Description")
        description = data.describe()
        st.write(description)

    # Data Manipulation
    st.subheader("Data Manipulation")
    st.write("Perform simple data transformation operations:")

    operation = st.selectbox("Select Operation", ["Select Columns", "Filter Rows", "Sort Data"])

    if operation == "Select Columns":
        selected_columns = st.multiselect("Select Columns", data.columns)
        if selected_columns:
            st.write(data[selected_columns])

    elif operation == "Filter Rows":
        column = st.selectbox("Select Column for Filtering", data.columns)
        value = st.text_input(f"Enter Value for {column}:", "")
        if value:
            filtered_data = data[data[column] == value]
            st.write(filtered_data)

    elif operation == "Sort Data":
        sort_column = st.selectbox("Select Column for Sorting", data.columns)
        ascending = st.checkbox("Ascending Order")
        sorted_data = data.sort_values(by=sort_column, ascending=ascending)
        st.write(sorted_data)
        
    # Data Cleaning Button
    if st.button("Clean Data"):
        cleaned_data = data.dropna().drop_duplicates()
        
        # Label Encoding
        label_encoder = LabelEncoder()
        categorical_columns = cleaned_data.select_dtypes(include=['object']).columns
        for col in categorical_columns:
            if col in cleaned_data.columns:
                cleaned_data[col] = label_encoder.fit_transform(cleaned_data[col])
        
        st.write("Data cleaned and encoded successfully!")
        data = cleaned_data


    # Conversion and Download
    st.subheader("Convert and Download")
    conversion_format = st.radio("Convert to:", ["CSV", "Excel"])
    if st.button("Convert and Download"):
        if conversion_format == "CSV":
            converted_file = io.BytesIO()
            data.to_csv(converted_file, index=False)
            st.download_button("Download Converted File", converted_file.getvalue(), file_name="converted_data.csv")
        elif conversion_format == "Excel":
            converted_file = io.BytesIO()
            data.to_excel(converted_file, index=False, engine='openpyxl')
            st.download_button("Download Converted File", converted_file.getvalue(), file_name="converted_data.xlsx")

    # Data Visualization
    st.sidebar.subheader("Choose Columns for Visualization")
    x_column = st.sidebar.selectbox("X Axis", data.columns)
    y_column = st.sidebar.selectbox("Y Axis", data.columns)

    st.subheader("Plotly Line Plot")

    if st.sidebar.button("Generate Plotly Line Plot"):
        fig = px.line(data, x=x_column, y=y_column, title='Line Plot')
        st.plotly_chart(fig, use_container_width=True)

# Reference Links    
link = 'Created by [Gideon Ogunbanjo](https://gideonogunbanjo.netlify.app)'
st.markdown(link, unsafe_allow_html=True)