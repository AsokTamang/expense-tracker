import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

projectroot = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print(projectroot)
sys.path.insert(0, projectroot)  # here we are appending the current file dir into a PYTHONPATH
from db.database import get_connection


def get_datas(start_date, end_date):
    with get_connection() as (cursor, db):
        data = pd.read_sql('''SELECT category,SUM(amount) AS total FROM expenses
                           WHERE expense_date BETWEEN %s AND %s
                           GROUP BY category;''',  db,params=[start_date,end_date])  # here db is our sql connecting instance\
        df = pd.DataFrame(data).plot(kind="bar",x='category')  # converting the data into dataframe using pd
        return df
print(get_datas('2024-08-01', '2024-09-02'))
plt.show()

