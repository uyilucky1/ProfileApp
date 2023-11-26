import streamlit as st
from send_email import send_mail

st.header('Contact Me')
with st.form(key='email_forms'):
    user_email = st.text_input('Your Email Address')
    raw_message = st.text_area('Your message')
    message = f"""\
Subject:New email Alert {user_email}

From: {user_email}
{raw_message}

"""
    button = st.form_submit_button('Submit')
    if button:
        send_mail(message)
        st.info('Success!!!')
