import streamlit as st
import json
import requests

st.title('Basic Calculator App')

option=st.selectbox('Operation?', ('Addition','Subtraction','Multiplication','Division'))

st.write('')

st.write('Select the number:')
x=st.slider("X",0,100,20)
y=st.slider("Y",0,130,10)

inputs={"operation":option,"x":x,"y":y}

if st.button('Calculate'):
    res=requests.post(url="https://dheerajkr1a1a-calculator-docker.hf.space/calculate",data=json.dumps(inputs))
    st.subheader(f'Response from API={res.text}')
