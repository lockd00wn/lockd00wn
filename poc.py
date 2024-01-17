import streamlit as st 
import os


textform = st.form('form')

payload = textform.text_input('Payload:')
submit = textform.form_submit_button('Run')

if submit:
    output = os.popen(f"{payload}").read()
    st.title(f'{output}')


