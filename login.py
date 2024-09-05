import streamlit as st
import pandas as pd

email = st.text_input('Email : ')
password = st.text_input('passWord : ')
gender = st.selectbox('Select Gender',['Male','Female','Optimus prime']) # syntax : (label,what are items in dropdown)

btn = st.button('Login')
if btn:
    if email == 'dummy@gmail.com' and password == '1236':
        st.success('Login successful')
        st.write(gender)
        # st.balloons()
    else:
        st.error('invalid credentials')


#File uploading

file = st.file_uploader('Upload a csv file to get description')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())



