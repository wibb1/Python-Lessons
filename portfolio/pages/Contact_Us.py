import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form('contact_form', clear_on_submit=True):
    user_email = st.text_input('Your email address')
    user_message = st.text_area('Your message')
    submitted = st.form_submit_button('Submit')
    outgoing_message = f"""\
Subject: Portfolio Email from {user_email}

From: {user_email}
{user_message}
"""
    if submitted:
        send_email(outgoing_message)
        st.info("Your email was sent")
