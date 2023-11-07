import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("Will Cmapbell")
    content = """Hi I'm Will, I am doing these small python apps to improve my skills since it has been a while since 
    I programmed in Python."""

    st.info(content)




