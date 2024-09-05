import streamlit as st
import pandas as pd
import time


st.title('Startup Dashboard')
st.header('This is heading')
st.subheader('This is subheading')

st.text('This is text written')

# creates heading # h1 ##h2 ### h3 and - , - BMW - indicates list type
st.markdown("""
## My cars 
- BMW
- AUDI
""")

# to show code
st.code("""
def multiply(a,b):
    return a*b
    
multiply(2,3)
""")

# latex used for showing some mathematical good representations
st.latex('x^2 + y^2 = 4') # it converts into ui understandable

# Displaying
df = pd.DataFrame({
    'name' : ['guy','gut','doom'],
    'rank' : [12,45,67],
    'packs': ['Family','SIX','Diamond']
})

st.dataframe(df)

#Metrics
st.metric('Bitcoin','2L','5%')

#json files
st.json({
    'name' : ['guy','gut','doom'],
    'rank' : [12,45,67],
    'packs': ['Family','SIX','Diamond']
})

#similarly for images and videoes

# st.image( -- image location or name if in current directory --)
# st.video(same same) .m4v types

#for adding sidebars
st.sidebar.title('Select options')

#adding columns
col1,col2 = st.columns(2)

with col1:
    st.json({
        'name': ['guy', 'gut', 'doom'],
        'rank': [12, 45, 67],
        'packs': ['Family', 'SIX', 'Diamond']
    })

with col2:
    st.latex('ax + by = c')

#progress bar
st.error('There is a mistake')
st.success('No Worries')
st.info('tips')
st.warning('Just a reminder')

bar = st.progress(0)

for i in range(1,100):
    time.sleep(0.01)
    bar.progress(i)


#Taking user inputs
email = st.text_input("Enter your email")
number = st.number_input('Enter your age :')
st.date_input('Enter DOB: ')

