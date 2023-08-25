import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import io
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


def main():
    st.sidebar.title("GraphGia - Data Cleaning & Exploration Tool")
    st.sidebar.write(
        "GraphGia is a tool for Data Cleaning, Visualization, and Exploratory Data Analysis."
    )
    st.sidebar.write("🫶")
    app_mode = st.sidebar.selectbox(
        "Choose the app mode", ["GraphGia", "EDA Dashboard"]
    )

    if app_mode == "GraphGia":
        graphgia()
    elif app_mode == "EDA Dashboard":
        eda_dashboard()


# GraphGia
def generate_analysis_code(data):
    analysis_code = f"""
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.preprocessing import LabelEncoder

    # Load the data
    data = pd.read_csv('your_uploaded_data.csv')

    # Display basic dataset statistics
    print("Dataset Statistics: ")
    print(data.describe())

    # Data Manipulation
    print("Data Manipulation")

    # ... (replace this section with your actual data manipulation code)

    # Data Cleaning
    print("Data Cleaning")
    cleaned_data = data.dropna().drop_duplicates()

    #Label Encoding
    label_encoder = LabelEncoder()
    categorical_columns = cleaned_data.select_dtypes(include=["object"]).columns
    for col in categorical_columns:
        if col in cleaned_data.columns:
            cleaned_data[col] = label_encoder.fit_transform(cleaned_data[col])

    print("Data cleaned and encoded successfully!")
    data = cleaned_data
    """

    return analysis_code


def graphgia():
    st.set_option("deprecation.showPyplotGlobalUse", False)
    st.title("GraphGia - Data Cleaning & Exploration Tool")
    st.write("This is a data cleaning & exploration tool.")

    # File Uploader Widget
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        if uploaded_file.name.endswith("csv"):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith("xlsx"):
            data = pd.read_excel(uploaded_file, engine="openpyxl")
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")

        st.write("Uploaded Data:", data)

        # Additional Information Button - Data Description
        if st.button("Show Extended Dataset Information"):
            st.subheader("Dataset Description")
            description = data.describe()
            st.write(description)

        # Generate Code Analysis
        if st.button("Generate Code Analysis"):
            analysis_code = generate_analysis_code(data)

            st.subheader("Generated Code Analysis")
            st.code(analysis_code, language="python")

            # # Download link for the generated code
            # st.download_button(
            #     label="Download Code Analysis",
            #     data=analysis_code,
            #     file_name="analysis_code.py",
            #     mime="text/plain",
            # )


# EDA Dashboard
def eda_dashboard():
    st.title("EDA Dashboard")
    st.write("This is an exploratory data analysis dashboard.")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("Dataset Statistics:")
        st.write(df.describe())

        # Checkbox for user-selected visualizations
        st.sidebar.title("Select Visualizations")
        histogram = st.sidebar.checkbox("Histogram")
        scatter_plot = st.sidebar.checkbox("Scatter Plot")
        correlation_matrix = st.sidebar.checkbox("Correlation Matrix")
        bar_chart = st.sidebar.checkbox("Bar Chart")
        scatter_matrix = st.sidebar.checkbox("Scatter Matrix")
        box_plot = st.sidebar.checkbox("Box Plot")
        pair_plot = st.sidebar.checkbox("Pair Plot")
        count_plot = st.sidebar.checkbox("Count Plot")

        # Histogram
        if histogram:
            st.subheader("Histogram")
            column = st.selectbox("Select a column for the histogram", df.columns)
            plt.hist(df[column], bins=20, edgecolor="k")
            st.pyplot()

            # Generated Histogram Code
            st.write("**Generated Histogram Code:**")
            hist_code = f"""
            import matplotlib.pyplot as plt
            column = '{column}'
            plt.hist(df[column], bins=20, edgecolor='k')
            plt.xlabel('{column}')
            plt.ylabel('Frequency')
            plt.title('Histogram of {column}')
            plt.show()
            """
            st.code(hist_code, language="python")

        # Scatter Plot
        if scatter_plot:
            st.subheader("Scatter Plot")
            x_column = st.selectbox("Select X-axis column", df.columns)
            y_column = st.selectbox("Select Y-axis column", df.columns)
            plt.scatter(df[x_column], df[y_column])
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            st.pyplot()

            # Generated Scatter Plot Code
            st.write("**Generated Scatter Plot Code:**")
            scatter_code = f"""
            import matplotlib.pyplot as plt
            x_column = '{x_column}'
            y_column = '{y_column}'
            plt.scatter(df[x_column], df[y_column])
            plt.xlabel('{x_column}')
            plt.ylabel('{y_column}')
            plt.title('Scatter Plot: {x_column} vs {y_column}')
            plt.show()
            """
            st.code(scatter_code, language="python")

        # Correlation Matrix
        if correlation_matrix:
            st.subheader("Correlation Matrix")
            corr_matrix = df.corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0)
            st.pyplot()

            # Generated Correlation Matrix Code
            st.write("**Generated Correlation Matrix Code**")
            corr_code = f"""
            import seaborn as sns
            import matplotlib.pyplot as plt
            corr_matrix = df.corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
            plt.title('Correlation Matrix')
            plt.show()
            """
            st.code(corr_code, language="python")

        # Bar Chart
        if bar_chart:
            st.subheader("Bar Chart")
            bar_column = st.selectbox("Select a column for the bar chart", df.columns)
            bar_chart = px.bar(df, x=bar_column)
            st.plotly_chart(bar_chart, use_container_width=True)

            # Generated Bar Chart Code
            st.write("**Generated Bar Chart Code**")
            bar_code = f"""
            import plotly.express as px
            bar_column = '{bar_column}'
            bar_chart = px.bar(df, x=bar_column)
            bar_chart.show()
            """
            st.code(bar_code, language="python")

        # Scatter Matrix
        if scatter_matrix:
            st.subheader("Scatter Matrix Plot")
            scatter_matrix = px.scatter_matrix(
                df, dimensions=df.columns, title="Scatter Matrix"
            )
            st.plotly_chart(scatter_matrix, use_container_width=True)

            # Generated Scatter Matrix Code
            st.write("**Generated Scatter Matrix Code**")
            scatter_matrix_code = f"""
            import plotly.express as px
            scatter_matrix = px.scatter_matrix(df, dimensions=df.columns, title='Scatter Matrix')
            scatter_matrix.show()
            """
            st.code(scatter_matrix_code, language="python")
            
        # Box Plot
        if box_plot:
            box_column = st.selectbox("Select a column for the box plot", df.columns)
            plt.boxplot(df[box_column])
            plt.xlabel(box_column)
            plt.ylabel("Value")
            st.pyplot()
            
            # Generated Box Plot Code
            st.write("**Generated Box Plot Code**")
            box_code = f"""
            box_column = '{box_column}'
            plt.boxplot(df[box_column])
            plt.xlabel('{box_column}')
            plt.ylabel('Value')
            plt.title('Box Plot: {box_column}')
            plt.show()
            """
            st.code(box_code, language="python")
        
        # Pair Plot
        if pair_plot:
            pair_plot = sns.pairplot(df)
            st.pyplot()

            # Generated Pair Plot Code
            st.write("**Generated Pair Plot Code**")
            pair_plot_code = """
            import seaborn as sns
            pair_plot = sns.pairplot(df)
            plt.show()
            """
            st.code(pair_plot_code, language="python")
            
        # Count Plot
        if count_plot:
            # Count Plot
            count_column = st.selectbox("Select a column for the count plot", df.columns)
            count_plot = sns.countplot(data=df, x=count_column)
            st.pyplot()

            # Generated Count Plot Code
            st.write("**Generated Count Plot Code**")
            count_plot_code = f"""
            count_column = '{count_column}'
            count_plot = sns.countplot(data=df, x='{count_column}')
            plt.show()
            """
            st.code(count_plot_code, language="python")






if __name__ == "__main__":
    main()

link = "Created by [Gideon Ogunbanjo](https://gideonogunbanjo.netlify.app)"
st.markdown(link, unsafe_allow_html=True)
