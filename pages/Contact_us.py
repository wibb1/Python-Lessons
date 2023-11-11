import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Us")
df = pandas.read_csv("topics.csv")
with st.form(key='contact_form', clear_on_submit=True):
    email = st.text_input("Tour Email Address", key="email_address")
    subject = st.selectbox("What topic do you want to discus", df['topics'], key='Subject')
    message = st.text_area("Text", height=25, key='Message')
    submitted = st.form_submit_button()

    if submitted:
        send_email(email, subject, message)
        st.info('Your email was sent!')

