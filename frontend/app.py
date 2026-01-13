import streamlit as st
import requests as rq
from datetime import datetime
import pandas as pd

api = "http://localhost:8000"  #this is our backend api

st.title('Expense Tracking System')
tab1,tab2=st.tabs(['Add/Update','Analytics'])

categories = ['Rent','Food','Shopping','Entertainment','Other']
with tab1:
    selected_date=st.date_input('Select Date',label_visibility='collapsed')
    response = rq.get(f'{api}/expenses/{selected_date}')
    if response.status_code == 200:
        data = response.json()

    else:
        st.error('No expenses found on this date')
        data = []

    with st.form(key='expenses'):
        column1, column2,column3 = st.columns(3)  #here we are makign 3 columns
        with column1:
            st.text('Amount')
        with column2:
            st.text('Category')
        with column3:
            st.text('Notes')
        for i in range(5):
            with column1:
                st.number_input('Amount',min_value=0.0,step=1.0,value=0.0,key=f'amount_{i}',label_visibility='collapsed')
            with column2:
                st.selectbox('Category',options =categories,key=f'category_{i}' ,label_visibility='collapsed')
            with column3:
               st.text_input(label='',value=" ",key=f'notes_{i}',label_visibility='collapsed')

        st.form_submit_button('Submit')


