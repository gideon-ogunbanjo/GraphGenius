# GraphGia - Data Visualization & Exploration Dashboard
### Overview

GraphGia is a simple data visualization dashboard built using Streamlit, designed to allow users to upload CSV or Excel files and perform various data visualization and exploration tasks.

### Features
- File Upload: GraphGia sllows users upload CSV or Excel files to visualize and explore data.
- Data Visualization: GraphGia generates a Plotly line plot and a seaborn heatmap based on chosen columns.
- Dataset Description: GraphGia displays extended statistical information about the dataset. It shows extended dataset information including data types and non-null counts.
- File Conversion: GraphGia allows users convert uploaded data between CSV and Excel formats.
- Data Cleaning: GraphGia allows users clean their uploaded data by removing duplicate and null values from the dataset
- File Download: GraphGia allows users download the converted file in the desired format.

### How to Use
1. Upload Data: Use the file uploader to select and upload a CSV or Excel file.
2. Dataset Description: View basic statistical information about the dataset.
3. Show Extended Information: Click the button to display additional dataset details.
4. Convert and Download: Convert the dataset between CSV and Excel formats and download the converted file.
5. Choose Columns for Visualization: Select the X and Y axes columns to generate a Plotly line plot.
### Dependencies
- Streamlit
- Pandas
- Matplotlib
- Plotly
- openpyxl
### Creator
Gideon Ogunbanjo.