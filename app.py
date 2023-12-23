import streamlit as st
import json
import requests

st.title('Basic Calculator App')

# Try to get the secret key from Streamlit secrets
try:
    url = st.secrets["secret"]
except KeyError:
    # If the secret key is not found, provide a default value
    url = st.text_input('Enter API URL:', type='password')

option = st.selectbox('Operation?', ('Addition', 'Subtraction', 'Multiplication', 'Division'))

st.write('')

st.write('Select the number:')
x = st.slider("X", 0, 100, 20)
y = st.slider("Y", 0, 130, 10)

inputs = {"operation": option, "x": x, "y": y}

if st.button('Calculate'):
    # Use the entered or default URL
    res = requests.post(url=url, data=json.dumps(inputs))
    st.subheader(f'Response from API = {res.text}')
