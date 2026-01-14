import streamlit as st
import pandas as pd
import requests

url = "http://localhost:8000"
def get_analyse(start_date,end_date):

    response = requests.post(f'{url}/expenses/analytics',json={'start_date':start_date.isoformat(),'end_date':end_date.isoformat()})
    datas = []
    total_values = sum([row['total'] for row in response.json()])
    for row in response.json():
        datas.append({
            'category': row['category'],
            'value': row['total'],
            'percentage': (row['total'] / total_values) * 100 if total_values != 0 else 0,

        })

    df=pd.DataFrame(datas,columns=['category','value','percentage'])   #setting the column
    st.bar_chart(df,x='category',y='value')
    df['value']=df['value'].astype(int)
    df['percentage']=df['percentage'].astype(int)
    st.table(df.set_index('category'))



