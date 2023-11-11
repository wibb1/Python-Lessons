import streamlit as st
import send_email

st.header("Contact Us")
with st.form(key='contact_form', clear_on_submit=True):
    email = st.text_input("Tour Email Address", key="email_address")
    subject = st.selectbox("What topic do you want to discus", ['Job Inquires', 'Project Proposals', 'Other'], key='Subject')
    message = st.text_area("Text", height=25, key='Message')
    outgoing_message = f"""
Subject: {subject}\n
From: {email}
\n {message}
"""
    submitted = st.form_submit_button()

    if submitted:
        send_email(message)

