import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("Will Cmapbell")
    content = """Hi I'm Will, I am doing these small python apps to improve my skills since it has been a while since 
    I programmed in Python."""

    st.info(content)

st.write("Below are some apps that I have built in Python.")

df = pandas.read_csv("data.csv", sep=";")
col3, col4 = st.columns(2)
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])



