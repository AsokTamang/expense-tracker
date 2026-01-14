import streamlit as st
import requests as rq
from datetime import datetime
import pandas as pd

api = "http://localhost:8000"  # this is our backend api

st.title('Expense Tracking System')
tab1, tab2 = st.tabs(['Add/Update', 'Analytics'])

with tab1:
    selected_date = st.date_input('Select Date', label_visibility='collapsed')
    response = rq.get(f'{api}/expenses/{selected_date}')
    if response.status_code == 200:
        data = response.json()
        st.write(data)
        expenses = []
        categories = ['Rent', 'Food', 'Shopping', 'Entertainment', 'Other']
        with st.form(key='expenses'):
            column1, column2, column3 = st.columns(3)  # here we are making 3 columns
            with column1:
                st.text('Amount')
            with column2:
                st.text('Category')
            with column3:
                st.text('Notes')
            if len(data) > 0:

                for i in range(len(data)):
                    amount = data[i][
                        'amount']  # here we are changing the value of the columns using the session_state with the help of key
                    category = data[i]['category']
                    notes = data[i]['notes']

                    with column1:
                        amount_input = st.number_input(label='Amount', min_value=0.0, step=1.0, value=amount,
                                                       label_visibility='collapsed')
                    with column2:
                        category_input = st.selectbox(label='Category', options=categories,
                                                      index=categories.index(category),
                                                      label_visibility='collapsed')
                    with column3:
                        note_input = st.text_input(label='Notes', value=notes,
                                                   label_visibility='collapsed')

                    expenses.append(
                        {
                            'amount': amount_input,
                            'category': category_input,
                            'notes': note_input
                        })
            else:
                for i in range(5):
                    with column1:
                        amount_input = st.number_input(label='Amount', min_value=0.0, step=1.0, value=0.0,
                                                       label_visibility='collapsed')
                    with column2:
                        category_input = st.selectbox(label='Category', options=categories,
                                                      index=categories.index('Rent'),
                                                      label_visibility='collapsed')
                    with column3:
                        note_input = st.text_input(label='Notes', value='',
                                                   label_visibility='collapsed')

                    expenses.append(
                        {
                            'amount': amount_input,
                            'category': category_input,
                            'notes': note_input
                        })

            submit_button = st.form_submit_button('Submit')
            if submit_button:

                filtered_data = [expense for expense in expenses if int(expense[
                                                                            'amount']) > 0]  # only if there is a valid expense we will add that expense data into our database
                if len(filtered_data) > 0:

                    response = rq.post(f'{api}/expenses/insert/{selected_date}', json=filtered_data)
                    if response.status_code == 200:
                        st.write(response.json())
                    else:
                        st.error('Failed to insert data')
                else:
                    st.error('Please insert valid data')
