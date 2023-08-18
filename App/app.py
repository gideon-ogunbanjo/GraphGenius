import streamlit as st

# Streamlit UI
st.set_page_config(
    page_title="GraphGenius",
    initial_sidebar_state="expanded",
    layout="centered"
)


def main():
    st.title("GraphGenius - Data Visualization Dashboard")
    st.write("GraphGenius is a data visualization dashboard. Users can upload CSV or Excel files to visualize and explore their data easily!")

if __name__ == "__main__":
    main()
