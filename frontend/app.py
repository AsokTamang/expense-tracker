import streamlit as st
import requests as rq
from datetime import datetime
import pandas as pd

api = "http://localhost:8000"  #this is our backend api

st.title('Expense Tracking System')
tab1,tab2=st.tabs(['Add/Update','Analytics'])

categories = ['Rent','Food','Shopping','Entertainment','Other']
with tab1:
    expenses = []
    selected_date=st.date_input('Select Date',label_visibility='collapsed')
    response = rq.get(f'{api}/expenses/{selected_date.strftime("%Y-%m-%d")}')
    if response.status_code == 200:
        data = response.json()


    else:
        st.error('No expenses found on this date')
        data = []

    with st.form(key='expenses'):
        column1, column2,column3 = st.columns(3)  #here we are making 3 columns
        with column1:
            st.text('Amount')
        with column2:
            st.text('Category')
        with column3:
            st.text('Notes')

        for i in range(5):
            if i<len(data):
                st.session_state[f'amount_{i}'] = data[i]['amount']    #here we are changing the value of the columns using the session_state with the help of key
                st.session_state[f'category_{i}'] = data[i]['category']
                st.session_state[f'notes_{i}'] = data[i]['notes']
            else:
                st.session_state[f'amount_{i}'] = 0.0
                st.session_state[f'category_{i}'] = "Rent"  #here we are making the rent category as default
                st.session_state[f'notes_{i}'] = ""

            with column1:
                amount_input = st.number_input(label='Amount',min_value=0.0,step=1.0,key=f'amount_{i}',label_visibility='collapsed')
            with column2:
               category_input =  st.selectbox(label='Category',options =categories  ,key=f'category_{i}' ,label_visibility='collapsed')
            with column3:
               note_input =  st.text_input(label='Notes',key=f'notes_{i}',label_visibility='collapsed')

            expenses.append(
                {
                    'amount':amount_input,
                    'category':category_input,
                    'notes':note_input
                }
            )


        submit_button=st.form_submit_button('Submit')
        if submit_button:
            filtered_data = [expense for expense in expenses if expense['amount']>0]  #only if there is a valid expense we will add that expense data into our database
            response=rq.post(f'{api}/expenses/insert/{selected_date}',json=filtered_data)
            if response.status_code==200:
                st.write('Inserted successfully')
            else:
                st.write('Failed to insert data')


