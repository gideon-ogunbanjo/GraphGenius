# GraphGia - Data Visualization & Exploration Tool
### Overview

GraphGia is a data visualization & Exploration tool, designed to allow users upload their CSV or Excel files and visualize, explore, clean and manipulate the uploaded data easily!

### Features
- File Upload: GraphGia sllows users upload CSV or Excel files to visualize and explore data.
- Data Visualization: GraphGia generates a Plotly line plot and a seaborn heatmap based on chosen columns.
- Dataset Description: GraphGia displays extended statistical information about the dataset. It shows extended dataset information including data types and non-null counts.
- Data Cleaning: GraphGia allows users clean their uploaded data by removing duplicate values, null values and label encoding data from the dataset
- File Download: GraphGia allows users download the converted file in the desired format.
- In-Built EDA Dashboard: GraphGia has an in-built exploratory data analysis dashboard that alows users Upload your dataset and explore it interactively!
- Code Generation for Data Analysis: GraphGia streamlines the data analysis process by generating code snippets that encapsulate crucial steps. Upon uploading a CSV or Excel file, the tool automatically loads the data and offers insights through descriptive statistics. Users can explore the data, manipulate it, and perform essential cleaning operations. GraphGia then generates Python code that reproduces these actions, fostering reproducibility in analysis.
- Code Snippets for Visualization: Enhancing data exploration, GraphGia generates code snippets for visualization. Users can select from a range of visualizations like histograms, scatter plots, correlation matrices, and more. As users interact with the data in the dashboard, the tool generates corresponding Python code snippets that can be integrated into projects. This feature accelerates the process of creating insightful visualizations for effective data communication.

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
- openpyxl. 
Dependencies are all listed in the `requirements.txt` file. 
### Creator
Gideon Ogunbanjo.