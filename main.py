import pandas as pd
import streamlit as st

if __name__ == '__main__':
    st.title("Weather Forcast for the Next Days")
    place = st.text_input(label="Place:")
    days = st.slider(label="Select data to view",min_value=1, max_value=5, step=1, help="Select a number of forecasted days")
    view_data = st.selectbox(label="Select data to view", options=["Temperature", "Sky"])
    if view_data == "Temperature":
        st.header(f"Temperature for the next {days} days in {place}")
    else:
        st.header("Sky")

