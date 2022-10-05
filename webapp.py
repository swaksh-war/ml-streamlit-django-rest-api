from readline import insert_text
import requests
import streamlit as st

result = ''

st.title("Let me Guess what can be you med!!!")

age = st.number_input('Insert Your Age', min_value=5, max_value=100)
gender = st.selectbox('Your Gender', ('Male','Female'))
bp = st.selectbox('Your Blood Pressure Level',('High', 'Low', 'Normal'))
cholesterol = st.selectbox('Your cholesterol level', ('High', 'Low', 'Normal'))
salt = st.number_input('Salt level in your body', min_value=4, max_value=50)
x = st.button('Predict')

if x:
    result = requests.post(f'http://127.0.0.1:8000/', data={'age':age,'gender':gender,'bp':bp,'cholesterol':cholesterol, 'salt':salt})

st.write(result.content.decode('ascii')[7:12])
