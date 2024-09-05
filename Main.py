import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df = pd.read_csv('cleaned_startup.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = round(df.groupby('startup')['amount'].sum().sort_values(ascending=False).head().values[0])
    # avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    # total funded startups
    num_startups = df['startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric('Total amount',str(total) + ' Cr')
    with col2:
        st.metric('Max amount', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg amount',str(round(avg_funding)) + ' Cr')
    with col4:
        st.metric('Funded Startups',num_startups)

    st.subheader('Month by month analysis')
    selected_option = st.selectbox('Select type',['Count','Total'])
    if selected_option == 'Count':
        df_y_m = df.groupby(['year', 'month'])['amount'].count().reset_index()
    else:
        df_y_m = df.groupby(['year', 'month'])['amount'].sum().reset_index()

    df_y_m['x_axis'] = df_y_m['month'].astype(str) + '-' + df_y_m['year'].astype(str)
    fig3, ax3 = plt.subplots()
    ax3.plot(df_y_m['x_axis'], df_y_m['amount'])

    st.pyplot(fig3)


# st.dataframe(df)
def load_investor_details(investor):
    st.title(investor)
    #print five investment details
    top5_df = df[df['investors'].str.contains(investor)][['date', 'startup', 'city', 'round', 'amount']].head()
    st.subheader('recent Investments')
    st.dataframe(top5_df)
    #biggest investments
    st.subheader('Top investments')
    big_inv = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
        ascending=False).head()
    # st.dataframe(big_inv)
    col1,col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        ax.bar(big_inv.index, big_inv.values)

        st.pyplot(fig)

    with col2:
        # st.dataframe(big_inv)
        df['year'] = df['date'].dt.year
        st.subheader('Year of year investment Graph')
        yoy_inv = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        fig1, ax1 = plt.subplots()
        ax1.plot(yoy_inv.index, yoy_inv.values)

        st.pyplot(fig1)



st.sidebar.title('Startup funding analysis')
option = st.sidebar.selectbox('Select one ',['overall Analysis','Startup','Investor'])

if option == 'overall Analysis':
    load_overall_analysis()
elif option == 'Startup':
    st.sidebar.selectbox('Select a startup',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Startup analysis')
    st.title('Startup Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select a Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Investor analysis')
    if btn2:
        load_investor_details(selected_investor)



