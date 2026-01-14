import streamlit as st
import pandas as pd
import requests

url = "http://localhost:8000"
def get_monthly_analyse(month):
    month_value={
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December',
    }

    response = requests.post(f'{url}/expenses/month_analytics/{month}')
    datas = []
    total_values = sum([row['total'] for row in response.json()])
    for row in response.json():
        datas.append({
            'category': row['category'],
            'value': row['total'],
            'percentage': (row['total'] / total_values) * 100 if total_values != 0 else 0,

        })

    df=pd.DataFrame(datas,columns=['category','value','percentage'])   #setting the column
    st.header(f'Monthly Analyse for month {month_value[month]}')
    st.bar_chart(df,x='category',y='value')
    df['value']=df['value'].astype(int)
    df['percentage']=df['percentage'].astype(int)
    st.table(df.set_index('category'))



