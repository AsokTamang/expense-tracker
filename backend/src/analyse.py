import pandas as pd
import os
import sys
projectroot=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print(projectroot)
sys.path.insert(0,projectroot)   #here we are appending the current file dir into a PYTHONPATH
from db.database import get_connection

with get_connection() as (cursor,db):
    data= pd.read_sql('SELECT * FROM expenses',db)  #here db is our sql connecting instance\
    df = pd.DataFrame(data) #converting the data into dataframe using pd
    print(df)


