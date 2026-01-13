from fastapi import FastAPI
import database

app = FastAPI()

@app.get('/expenses')
async def get_expenses():
    expenses =  database.get_all_datas()
    return expenses

